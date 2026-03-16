"""
Betweenness Centrality Baselines (Unweighted) — Brandes (2001)

This file generates baseline JSON outputs for TigerGraph's graph_algorithms_testing repo,
mirroring the JSON structure used by the other baseline generators.

Algorithm: Brandes Algorithm 1 (unweighted)
  - forward BFS builds: S, P, σ, d
  - backward accumulation builds δ and adds into BC

Output format:
  [{"top_scores": [{"Vertex_ID": "...", "score": <float>}, ...]}]

TigerGraph note:
  TigerGraph docs describe the final aggregation as:
    BC(v) = Σ_s PD_{s*}(v) / 2
  so we apply a final division by 2 in this baseline to match that convention. :contentReference[oaicite:1]{index=1}
"""

import csv
import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


# ----------------------------
# Types (match your repo style)
# ----------------------------

type VertexId = str
type Dist = int
type Sigma = float
type Delta = float
type BC = float

type VertexMap[T] = dict[VertexId, T]

type Neighbors = set[VertexId]
type Adjacency = VertexMap[Neighbors]

type Predecessors = list[VertexId]
type VertexPredecessors = VertexMap[Predecessors]

type VertexDist = VertexMap[Dist]
type VertexSigma = VertexMap[Sigma]
type VertexDelta = VertexMap[Delta]
type VertexBetweenness = VertexMap[BC]


# ----------------------------
# Graph interface + adjacency
# ----------------------------


class UnweightedGraph(Protocol):
    @property
    def directed(self) -> bool: ...

    def vertices(self) -> list[VertexId]: ...

    def neighbors(self, v: VertexId) -> Neighbors: ...


@dataclass(slots=True, kw_only=True)
class AdjacencyUnweighted:
    adjacency: Adjacency
    directed: bool = False

    def vertices(self) -> list[VertexId]:
        return list(self.adjacency.keys())

    def neighbors(self, v: VertexId) -> Neighbors:
        return self.adjacency[v]


# ----------------------------
# Brandes per-source state
# ----------------------------


@dataclass(slots=True, kw_only=True)
class ShortestPathState:
    """
    Per-source Brandes state:

      S        : stack of vertices in nondecreasing distance from s
      P[w]     : predecessors of w on shortest paths from s
      σ[w]     : # shortest paths from s to w
      d[w]     : distance from s to w
    """

    source: VertexId
    stack: list[VertexId]
    pred: VertexPredecessors
    sigma: VertexSigma
    dist: VertexDist

    @classmethod
    def initialize(
        cls, *, source: VertexId, vertices: list[VertexId]
    ) -> "ShortestPathState":
        dist: VertexDist = {v: -1 for v in vertices}
        sigma: VertexSigma = {v: 0.0 for v in vertices}
        pred: VertexPredecessors = {v: [] for v in vertices}
        stack: list[VertexId] = []
        return cls(source=source, stack=stack, pred=pred, sigma=sigma, dist=dist)


# ----------------------------
# Forward pass (BFS)
# ----------------------------


def forward_bfs(
    graph: UnweightedGraph,
    source: VertexId,
    *,
    vertices: list[VertexId],
) -> ShortestPathState:
    """
    Brandes Algorithm 1 — forward BFS from a single source s.

    Builds:
      - S: stack in nondecreasing distance order
      - P[w]: predecessors on shortest paths
      - σ[w]: number of shortest paths from s to w
      - d[w]: hop distance from s
    """
    state = ShortestPathState.initialize(source=source, vertices=vertices)

    state.dist[source] = 0
    state.sigma[source] = 1.0

    q: deque[VertexId] = deque([source])

    while q:
        v = q.popleft()
        state.stack.append(v)

        dv: Dist = state.dist[v]

        # Deterministic neighbor iteration (Neighbors is a set)
        for w in sorted(graph.neighbors(v)):
            if state.dist[w] < 0:
                state.dist[w] = dv + 1
                q.append(w)

            if state.dist[w] == dv + 1:
                state.sigma[w] += state.sigma[v]
                state.pred[w].append(v)

    return state


# ----------------------------
# Backward accumulation
# ----------------------------


def dependencies(state: ShortestPathState) -> VertexDelta:
    """
    Compute δ for a fixed source s (δ[v] ≡ δ_{s*}(v)).
    """
    delta: VertexDelta = {v: 0.0 for v in state.dist.keys()}

    for w in reversed(state.stack):
        sigma_w = state.sigma[w]
        if sigma_w == 0.0:
            # unreachable nodes shouldn't appear in stack; treat as invariant failure
            raise ValueError(f"sigma[{w}] is 0. Forward pass invariant violated.")

        coeff = (1.0 + delta[w]) / sigma_w
        for v in state.pred[w]:
            delta[v] += state.sigma[v] * coeff

    return delta


def accumulate(state: ShortestPathState, bc: VertexBetweenness) -> None:
    """
    Accumulate betweenness contribution for a single source s (endpoints excluded):
      BC[w] += δ[w] for w != s
    """
    delta = dependencies(state)
    s = state.source
    for w in state.stack:
        if w != s:
            bc[w] += delta[w]


def accumulate_endpoints(state: ShortestPathState, bc: VertexBetweenness) -> None:
    """
    Endpoint-included variant (NetworkX-style shape):
      BC[s] += |S| - 1
      BC[w] += δ[w] + 1 for w != s
    """
    s = state.source
    bc[s] += float(len(state.stack) - 1)

    delta: VertexDelta = {v: 0.0 for v in state.dist.keys()}

    for w in reversed(state.stack):
        sigma_w = state.sigma[w]
        if sigma_w == 0.0:
            raise ValueError(f"sigma[{w}] is 0. Forward pass invariant violated.")

        coeff = (1.0 + delta[w]) / sigma_w
        for v in state.pred[w]:
            delta[v] += state.sigma[v] * coeff

        if w != s:
            bc[w] += delta[w] + 1.0


# ----------------------------
# Post-processing
# ----------------------------


def normalize(
    bc: VertexBetweenness,
    *,
    n: int,
    directed: bool,
    endpoints: bool,
) -> None:
    """
    Optional normalization (NetworkX convention):
      directed:   divide by N(N-1)
      undirected: divide by N(N-1)/2
    where N = n if endpoints else n-1
    """
    if n <= 2:
        return

    N = n if endpoints else (n - 1)
    if N <= 1:
        return

    denom = N * (N - 1)
    scale = (1.0 / denom) if directed else (2.0 / denom)

    for v in bc:
        bc[v] *= scale


def calculate_score(
    graph: UnweightedGraph,
    *,
    normalized: bool = False,
    endpoints: bool = False,
) -> VertexBetweenness:
    """
    Compute betweenness centrality for all vertices (Brandes 2001, unweighted).
    """
    vertices = graph.vertices()
    bc: VertexBetweenness = {v: 0.0 for v in vertices}

    for s in vertices:
        state = forward_bfs(graph, s, vertices=vertices)
        if endpoints:
            accumulate_endpoints(state, bc)
        else:
            accumulate(state, bc)

    # Compute BC(v) = Σ_s PD_{s*}(v) / 2
    if not graph.directed:
        for v in bc:
            bc[v] *= 0.5
    if normalized:
        normalize(bc, n=len(vertices), directed=graph.directed, endpoints=endpoints)

    return bc


# ----------------------------
# I/O helpers for this repo
# ----------------------------


def _load_vertex_ids(path: Path) -> list[VertexId]:
    """
    Load vertex IDs from a CSV (one id per line OR id in first column).
    This repo has data/twenty_nodes.csv and data/eight_nodes.csv.
    """
    ids: list[VertexId] = []
    with path.open(newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            v = row[0].strip()
            if not v:
                continue
            ids.append(v)
    return ids


def _load_unweighted_edge_csv(path: Path) -> list[tuple[VertexId, VertexId]]:
    edges: list[tuple[VertexId, VertexId]] = []
    with path.open(newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if len(row) == 1 and row[0].strip() == "(empty)":
                continue
            u = row[0].strip()
            v = row[1].strip()
            edges.append((u, v))
    return edges


def _build_graph(
    *,
    vertices: list[VertexId],
    edges: list[tuple[VertexId, VertexId]],
    directed: bool,
) -> AdjacencyUnweighted:
    adjacency: Adjacency = {v: set() for v in vertices}

    def ensure(v: VertexId) -> None:
        if v not in adjacency:
            adjacency[v] = set()

    for u, v in edges:
        ensure(u)
        ensure(v)
        adjacency[u].add(v)
        if not directed:
            adjacency[v].add(u)

    return AdjacencyUnweighted(adjacency=adjacency, directed=directed)


def _format_baseline(
    scores: VertexBetweenness,
) -> list[dict[str, list[dict[str, float]]]]:
    # Deterministic ordering by Vertex_ID (tests usually sort anyway)
    out = [{"Vertex_ID": v, "score": float(scores[v])} for v in sorted(scores)]
    return [{"top_scores": out}]


# ----------------------------
# Baseline generator entrypoint
# ----------------------------


def run() -> None:
    data_root = Path("data")
    edges_root = data_root / "unweighted_edges"

    out_root = data_root / "baseline" / "centrality" / "betweenness"
    out_root.mkdir(parents=True, exist_ok=True)

    v20 = _load_vertex_ids(data_root / "twenty_nodes.csv")

    jobs: list[tuple[str, bool, str]] = [
        ("empty_graph_edges.csv", False, "Empty.json"),
        ("hubspoke_edges.csv", False, "Hub_Spoke.json"),
        ("hubspoke_edges.csv", True, "Hub_Spoke_Directed.json"),
        ("line_edges.csv", False, "Line.json"),
        ("line_edges.csv", True, "Line_Directed.json"),
        ("ring_edges.csv", False, "Ring.json"),
        ("ring_edges.csv", True, "Ring_Directed.json"),
        ("tree_edges.csv", False, "Tree.json"),
        ("tree_edges.csv", True, "Tree_Directed.json"),
    ]

    for csv_name, directed, out_name in jobs:
        edges = _load_unweighted_edge_csv(edges_root / csv_name)
        graph = _build_graph(vertices=v20, edges=edges, directed=directed)

        scores = calculate_score(graph, normalized=False, endpoints=False)
        payload = _format_baseline(scores)

        out_path = out_root / out_name
        with out_path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(payload, f)
            _ = f.write("\n")

        print(f"Wrote {out_path}")


if __name__ == "__main__":
    run()
