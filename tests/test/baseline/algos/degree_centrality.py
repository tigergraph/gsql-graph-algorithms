from collections import Counter
from functools import partial

import networkx as nx

from .base import Baseline
from .common import create_baseline


def run_degree_baseline_complete(g: nx.Graph, _):
    s = 1.0 / (len(g) - 1.0)

    # d-1 because nx will double count the self-edge
    res = {n: (d - 1) * s for n, d in g.degree()}

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def run_degree_baseline(g: nx.Graph, metric):
    res = metric(g)

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def weighted_deg_cent(
    g: nx.Graph,
    dir: str = "",
):
    res = Counter()
    for e in g.edges:
        a = g.get_edge_data(e[0], e[1])["weight"]
        match dir:
            case "in":
                res[e[1]] += a
            case "out":
                res[e[0]] += a
            case _:
                res[e[0]] += a
                res[e[1]] += a
    return res


class DegreeCentralityBaseline(Baseline):
    def __init__(self, data_path_root, baseline_path_root):
        self.data_path_root = data_path_root
        self.baseline_path_root = baseline_path_root

    def run(self):
        # (data, output_path, fun, metric)
        paths = [
            # unweighted
            (
                f"{self.data_path_root}/unweighted_edges/complete_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/Complete.json",
                run_degree_baseline_complete,
                None,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/Line.json",
                run_degree_baseline,
                nx.centrality.degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/Ring.json",
                run_degree_baseline,
                nx.centrality.degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/Hub_Spoke.json",
                run_degree_baseline,
                nx.centrality.degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/Tree.json",
                run_degree_baseline,
                nx.centrality.degree_centrality,
            ),
            # in_degree
            (
                f"{self.data_path_root}/unweighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/in_degree/Line_Directed.json",
                run_degree_baseline,
                nx.centrality.in_degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/in_degree/Ring_Directed.json",
                run_degree_baseline,
                nx.centrality.in_degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/in_degree/Hub_Spoke_Directed.json",
                run_degree_baseline,
                nx.centrality.in_degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/in_degree/Tree_Directed.json",
                run_degree_baseline,
                nx.centrality.in_degree_centrality,
            ),
            # out_degree
            (
                f"{self.data_path_root}/unweighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/out_degree/Line_Directed.json",
                run_degree_baseline,
                nx.centrality.out_degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/out_degree/Ring_Directed.json",
                run_degree_baseline,
                nx.centrality.out_degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/out_degree/Hub_Spoke_Directed.json",
                run_degree_baseline,
                nx.centrality.out_degree_centrality,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/degree_centrality/out_degree/Tree_Directed.json",
                run_degree_baseline,
                nx.centrality.out_degree_centrality,
            ),
            # weighted
            (
                f"{self.data_path_root}/weighted_edges/complete_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/Complete_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent),
            ),
            (
                f"{self.data_path_root}/weighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/Line_Weighted.json",
                run_degree_baseline,
                weighted_deg_cent,
            ),
            (
                f"{self.data_path_root}/weighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/Ring_Weighted.json",
                run_degree_baseline,
                weighted_deg_cent,
            ),
            (
                f"{self.data_path_root}/weighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/Hub_Spoke_Weighted.json",
                run_degree_baseline,
                weighted_deg_cent,
            ),
            (
                f"{self.data_path_root}/weighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/Tree_Weighted.json",
                run_degree_baseline,
                weighted_deg_cent,
            ),
            # in_degree
            (
                f"{self.data_path_root}/weighted_edges/complete_edges_directed.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Complete_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="in"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Line_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="in"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Ring_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="in"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Hub_Spoke_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="in"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Tree_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="in"),
            ),
            # out_degree
            (
                f"{self.data_path_root}/weighted_edges/complete_edges_directed.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Complete_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="out"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Line_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="out"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Ring_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="out"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Hub_Spoke_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="out"),
            ),
            (
                f"{self.data_path_root}/weighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Tree_Directed_Weighted.json",
                run_degree_baseline,
                partial(weighted_deg_cent, dir="out"),
            ),
        ]
        create_baseline(paths, "degree centrality")
