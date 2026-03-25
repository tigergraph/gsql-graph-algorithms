from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

import pytest
import pyTigerGraph as tg
from dotenv import load_dotenv

load_dotenv()

QUERY_NAME = "tg_betweenness_centrality"


@dataclass(frozen=True, slots=True)
class Case:
    name: str
    edge_type: str
    vertex_type: str
    directed: bool


CASES: tuple[Case, ...] = (
    Case("Empty", "Empty", "V20", False),
    Case("Line", "Line", "V20", False),
    Case("Ring", "Ring", "V20", False),
    Case("Hub_Spoke", "Hub_Spoke", "V20", False),
    Case("Tree", "Tree", "V20", False),
    Case("Line_Directed", "Line_Directed", "V20", True),
    Case("Ring_Directed", "Ring_Directed", "V20", True),
    Case("Hub_Spoke_Directed", "Hub_Spoke_Directed", "V20", True),
    Case("Tree_Directed", "Tree_Directed", "V20", True),
)


def _load_json(path: Path) -> object:
    return json.loads(path.read_text())


def _score_map(payload: object) -> dict[str, float]:
    """
    Expected payload shape:
    [
      {
        "top_scores": [
          {"Vertex_ID": "...", "score": ...},
          ...
        ]
      }
    ]
    """
    if not isinstance(payload, list) or not payload:
        raise AssertionError(f"Unexpected payload shape: {type(payload)} {payload!r}")

    first = payload[0]
    if not isinstance(first, dict):
        raise AssertionError(f"Unexpected payload[0] shape: {type(first)} {first!r}")

    top_scores = first.get("top_scores")
    if not isinstance(top_scores, list):
        raise AssertionError(f"Missing/invalid top_scores: {top_scores!r}")

    scores: dict[str, float] = {}
    for row in top_scores:
        if not isinstance(row, dict):
            raise AssertionError(f"Bad score row: {row!r}")

        vertex_id = row.get("Vertex_ID")
        score = row.get("score")
        if vertex_id is None or score is None:
            raise AssertionError(f"Missing keys in row: {row!r}")

        scores[str(vertex_id)] = float(score)

    return scores


def _reverse_e_type(edge_type: str, directed: bool) -> list[str]:
    if directed:
        return [f"reverse_{edge_type}"]
    return [edge_type]


def _query_params(case: Case) -> dict[str, object]:
    return {
        "v_type_set": [case.vertex_type],
        "e_type_set": [case.edge_type],
        "reverse_e_type": _reverse_e_type(case.edge_type, case.directed),
        "max_hops": 100,
        "top_k": 1000,
        "print_results": True,
        "result_attribute": "",
        "file_path": "",
        "display_edges": False,
    }


class TestBetweenness:
    conn = tg.TigerGraphConnection(
        host=os.getenv("HOST_NAME"),
        username=os.getenv("USER_NAME"),
        password=os.getenv("PASS"),
        graphname="graph_algorithms_testing",
    )

    if os.environ.get("USE_TKN", "true").lower() == "true":
        conn.getToken()

    @pytest.mark.parametrize("case", CASES, ids=lambda c: c.name)
    def test_betweenness_unweighted(self, case: Case) -> None:
        baseline_path = Path(f"data/baseline/centrality/betweenness/{case.name}.json")
        baseline = _score_map(_load_json(baseline_path))

        params = _query_params(case)
        result_json = self.conn.runInstalledQuery(QUERY_NAME, params=params)
        result = _score_map(result_json)

        assert result.keys() == baseline.keys(), (
            f"{case.name}: key mismatch.\n"
            f"Missing: {sorted(baseline.keys() - result.keys())}\n"
            f"Extra: {sorted(result.keys() - baseline.keys())}\n"
            f"query={QUERY_NAME!r}, reverse_e_type={params['reverse_e_type']!r}"
        )

        for vertex_id, expected in baseline.items():
            got = result[vertex_id]
            assert got == pytest.approx(expected, rel=1e-12, abs=1e-12), (
                f"{case.name}: {vertex_id}: got={got} expected={expected} "
                f"(query={QUERY_NAME!r}, reverse_e_type={params['reverse_e_type']!r})"
            )
