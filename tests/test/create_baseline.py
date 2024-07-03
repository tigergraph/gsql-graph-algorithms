import csv
import json
from collections import Counter
from functools import partial

import networkx as nx
import numpy as np
from tqdm import tqdm

data_path_root = "data/"
baseline_path_root = f"{data_path_root}/baseline/"


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


def create_graph(edges, weights=False, directed=False):
    if directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    if weights:
        # make weights floats
        edges = [[a, b, float(c)] for a, b, c in edges]
        g.add_weighted_edges_from(edges)
    else:
        g.add_edges_from(edges)
    return g


def create_degree_baseline(paths):
    t = tqdm(paths, desc="Creating baselines")
    for p, out_path, fn, m in t:
        t.set_postfix_str(out_path.split("/")[-1].split(".")[0])
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        directed = True if "Directed" in out_path else False
        weights = True if "Weighted" in out_path else False
        g = create_graph(edges, weights, directed)

        # from matplotlib import pyplot as plt
        # pos = nx.drawing.layout.kamada_kawai_layout(g)
        # nx.draw(g, pos)
        # nx.draw_networkx_labels(g, pos, {n: n for n in g.nodes})
        # plt.savefig(f"{out_path.split('/')[-1]}.png")

        res = fn(g, m)
        with open(out_path, "w") as f:
            json.dump(res, f)  # , indent=2)


if __name__ == "__main__":
    # (data, output_path, fun, metric)
    paths = [
        # unweighted
        (
            f"{data_path_root}/unweighted_edges/complete_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Complete.json",
            run_degree_baseline_complete,
            None,
        ),
        (
            f"{data_path_root}/unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Line.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Ring.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Hub_Spoke.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Tree.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        # in_degree
        (
            f"{data_path_root}/unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Line_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Ring_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Hub_Spoke_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Tree_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        # out_degree
        (
            f"{data_path_root}/unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Line_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Ring_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Hub_Spoke_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        (
            f"{data_path_root}/unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Tree_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        # weighted
        (
            f"{data_path_root}/weighted_edges/complete_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/Complete_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent),
        ),
        (
            f"{data_path_root}/weighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/Line_Weighted.json",
            run_degree_baseline,
            weighted_deg_cent,
        ),
        (
            f"{data_path_root}/weighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/Ring_Weighted.json",
            run_degree_baseline,
            weighted_deg_cent,
        ),
        (
            f"{data_path_root}/weighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/Hub_Spoke_Weighted.json",
            run_degree_baseline,
            weighted_deg_cent,
        ),
        (
            f"{data_path_root}/weighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/Tree_Weighted.json",
            run_degree_baseline,
            weighted_deg_cent,
        ),
        # in_degree
        (
            f"{data_path_root}/weighted_edges/complete_edges_directed.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Complete_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="in"),
        ),
        (
            f"{data_path_root}/weighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Line_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="in"),
        ),
        (
            f"{data_path_root}/weighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Ring_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="in"),
        ),
        (
            f"{data_path_root}/weighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Hub_Spoke_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="in"),
        ),
        (
            f"{data_path_root}/weighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/in_degree/Tree_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="in"),
        ),
        # out_degree
        (
            f"{data_path_root}/weighted_edges/complete_edges_directed.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Complete_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="out"),
        ),
        (
            f"{data_path_root}/weighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Line_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="out"),
        ),
        (
            f"{data_path_root}/weighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Ring_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="out"),
        ),
        (
            f"{data_path_root}/weighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Hub_Spoke_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="out"),
        ),
        (
            f"{data_path_root}/weighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/weighted_degree_centrality/out_degree/Tree_Directed_Weighted.json",
            run_degree_baseline,
            partial(weighted_deg_cent, dir="out"),
        ),
    ]
    create_degree_baseline(paths)
