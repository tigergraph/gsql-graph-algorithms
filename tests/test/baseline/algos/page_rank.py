import networkx as nx


def tg_pagerank(
    g: nx.Graph,
    damping: float = 0.85,
    max_change: float = 0.05,
    maximum_iteration: int = 10,
):
    """Replicates TigerGraph's tg_pagerank GSQL query exactly.

    Key GSQL behaviour reproduced here:
        - Every vertex starts with score = 1.0
        - Each iteration, ONLY vertices that have outgoing edges (appear as 's'
          in the FROM clause) get their score updated via POST-ACCUM.
          Vertices with out-degree 0 are never selected as 's', so their score
          stays at 1.0 for the entire run.
        - For undirected graphs every vertex has degree >= 1 (assuming no
          isolated nodes), so all vertices are updated each iteration.
        - Stops when max score change across updated vertices <= max_change,
          or maximum_iteration is reached.

    Parameters match what the existing baselines were generated with:
        damping=0.85, max_change=0.05, maximum_iteration=25
    """
    nodes = list(g.nodes())
    scores = {n: 1.0 for n in nodes}

    for _ in range(maximum_iteration):
        # Accumulate received scores into a temp dict (all nodes start at 0)
        recvd = {n: 0.0 for n in nodes}
        for u in nodes:
            out_deg = g.out_degree(u) if g.is_directed() else g.degree(u)
            if out_deg == 0:
                continue
            for v in (g.successors(u) if g.is_directed() else g.neighbors(u)):
                recvd[v] += scores[u] / out_deg

        max_diff = 0.0
        new_scores = dict(scores)  # copy — preserves score=1.0 for out-deg-0 nodes

        for u in nodes:
            out_deg = g.out_degree(u) if g.is_directed() else g.degree(u)
            if out_deg == 0:
                # GSQL never selects this vertex as 's' → score never changes
                continue
            updated = (1.0 - damping) + damping * recvd[u]
            max_diff = max(max_diff, abs(updated - scores[u]))
            new_scores[u] = updated

        scores = new_scores
        if max_diff <= max_change:
            break

    return scores


def tg_pagerank_wt(
    g: nx.Graph,
    damping: float = 0.85,
    max_change: float = 0.05,
    maximum_iteration: int = 10,
):
    """Replicates TigerGraph's tg_pagerank_wt GSQL query exactly.

    Same POST-ACCUM scoping rule as tg_pagerank: only vertices with
    outgoing edges (total_wt > 0) get their score updated each iteration.

    Parameters match what the existing baselines were generated with:
        damping=0.85, max_change=0.05, maximum_iteration=25
    """
    nodes = list(g.nodes())
    scores = {n: 1.0 for n in nodes}

    # Pre-compute total outgoing weight per node (matches GSQL's @sum_total_wt)
    total_wt = {}
    for u in nodes:
        neighbors = list(g.successors(u)) if g.is_directed() else list(g.neighbors(u))
        total_wt[u] = sum(g[u][nbr].get("weight", 1.0) for nbr in neighbors)

    for _ in range(maximum_iteration):
        recvd = {n: 0.0 for n in nodes}
        for u in nodes:
            if total_wt[u] == 0:
                continue
            for v in (g.successors(u) if g.is_directed() else g.neighbors(u)):
                edge_wt = g[u][v].get("weight", 1.0)
                recvd[v] += scores[u] * edge_wt / total_wt[u]

        max_diff = 0.0
        new_scores = dict(scores)  # preserves score=1.0 for zero-weight nodes

        for u in nodes:
            if total_wt[u] == 0:
                # GSQL never selects this vertex as 's' → score never changes
                continue
            updated = (1.0 - damping) + damping * recvd[u]
            max_diff = max(max_diff, abs(updated - scores[u]))
            new_scores[u] = updated

        scores = new_scores
        if max_diff <= max_change:
            break

    return scores


def run_pagerank_baseline(g: nx.Graph, metric):
    """Generic runner for tg_pagerank / tg_pagerank_wt.

    Output format matches TigerGraph's GSQL PageRank baseline:
      - Key is @@top_scores_heap
      - Scores are raw (around 1.0), matching GSQL's initial score=1.0
      - Results are sorted descending by score
    """
    res = metric(g)

    out = sorted(
        [{"Vertex_ID": k, "score": round(v, 7)} for k, v in res.items()],
        key=lambda x: x["score"],
        reverse=True,
    )
    return [{"@@top_scores_heap": out}]