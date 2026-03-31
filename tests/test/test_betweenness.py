from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

import pytest
import pyTigerGraph as tg
from dotenv import load_dotenv

load_dotenv()

QUERY_NAME = "tg_betweenness_cent"

HERE = Path(__file__).resolve().parent
TESTS_ROOT = HERE.parent
DATA_ROOT = TESTS_ROOT / "data"
BASELINE_ROOT = DATA_ROOT / "baseline" / "centrality" / "betweenness"


@dataclass(frozen=True, slots=True)
class Case:
    name: str
    edge_type: str
    vertex_type: str
    directed: bool
    baseline_file: str


CASES: tuple[Case, ...] = (
    Case("Empty", "Empty", "V20", False, "Empty.json"),
    Case("Hub_Spoke", "Hub_Spoke", "V20", False, "Hub_Spoke.json"),
    Case(
        "Hub_Spoke_Directed",
        "Hub_Spoke_Directed",
        "V20",
        True,
        "Hub_Spoke_Directed.json",
    ),
    Case("Line", "Line", "V20", False, "Line.json"),
    Case("Line_Directed", "Line_Directed", "V20", True, "Line_Directed.json"),
    Case("Ring", "Ring", "V20", False, "Ring.json"),
    Case("Ring_Directed", "Ring_Directed", "V20", True, "Ring_Directed.json"),
    Case("Tree", "Tree", "V20", False, "Tree.json"),
    Case("Tree_Directed", "Tree_Directed", "V20", True, "Tree_Directed.json"),
)


def load_json_file(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def reverse_edge_types(edge_type: str, directed: bool) -> list[str]:
    return [f"reverse_{edge_type}"] if directed else [edge_type]


def build_query_params(case: Case) -> dict[str, object]:
    return {
        "v_type_set": [case.vertex_type],
        "e_type_set": [case.edge_type],
        "reverse_e_type": reverse_edge_types(case.edge_type, case.directed),
        "max_hops": 100,
        "top_k": 1000,
        "print_results": True,
        "result_attribute": "",
        "file_path": "",
        "display_edges": False,
    }


def payload_to_score_map(payload: object) -> dict[str, float]:
    """
    Expected payload shape:
    [
        {
            "top_scores": [
                {"Vertex_ID": "A", "score": 0.0},
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


def compare_score_maps(
    *,
    case_name: str,
    actual: dict[str, float],
    expected: dict[str, float],
    query_name: str,
    params: dict[str, object],
    raw_result: object,
    baseline_path: Path,
    rel: float = 1e-12,
    abs_: float = 1e-12,
) -> None:
    actual_keys = set(actual)
    expected_keys = set(expected)

    missing = sorted(expected_keys - actual_keys)
    extra = sorted(actual_keys - expected_keys)

    mismatches: list[tuple[str, float, float, float, float]] = []
    # (vertex_id, got, expected, abs_diff, rel_diff)

    for vertex_id in sorted(expected_keys & actual_keys):
        got = actual[vertex_id]
        want = expected[vertex_id]
        abs_diff = abs(got - want)

        if abs(want) <= abs_:
            rel_diff = 0.0 if abs_diff <= abs_ else float("inf")
        else:
            rel_diff = abs_diff / abs(want)

        if abs_diff > abs_ and rel_diff > rel:
            mismatches.append((vertex_id, got, want, abs_diff, rel_diff))

    if not missing and not extra and not mismatches:
        return

    lines: list[str] = [f"{case_name}: query output does not match baseline"]

    if missing:
        lines.append(f"missing vertex IDs ({len(missing)}): {missing}")

    if extra:
        lines.append(f"extra vertex IDs ({len(extra)}): {extra}")

    if mismatches:
        lines.append(f"incorrect scores ({len(mismatches)}):")
        for vertex_id, got, want, abs_diff, rel_diff in mismatches:
            lines.append(
                f"  {vertex_id}: got={got}, expected={want}, "
                f"abs_diff={abs_diff}, rel_diff={rel_diff}"
            )

    lines.append(f"baseline_path={baseline_path}")
    lines.append(f"query={query_name!r}")
    lines.append(f"params={params!r}")
    lines.append(f"raw_result={raw_result!r}")

    raise AssertionError("\n".join(lines))


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
    def test_query_matches_baseline(self, case: Case) -> None:
        baseline_path = BASELINE_ROOT / case.baseline_file
        baseline_payload = load_json_file(baseline_path)
        expected_scores = payload_to_score_map(baseline_payload)

        params = build_query_params(case)
        raw_result = self.conn.runInstalledQuery(QUERY_NAME, params=params)

        # Fail immediately if the query returned no rows at all.
        actual_scores = payload_to_score_map(raw_result)

        compare_score_maps(
            case_name=case.name,
            actual=actual_scores,
            expected=expected_scores,
            query_name=QUERY_NAME,
            params=params,
            raw_result=raw_result,
            baseline_path=baseline_path,
        )
