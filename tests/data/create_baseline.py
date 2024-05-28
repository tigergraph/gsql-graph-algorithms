import csv
import json

import networkx as nx
import numpy as np
from tqdm import tqdm

baseline_path_root = "baseline"


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
        g.add_weighted_edges_from(edges)
    else:
        g.add_edges_from(edges)
    return g


def create_degree_baseline():
    # input, output, weighed
    paths = [
        (
            "unweighted_edges/complete_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Complete.json",
            run_degree_baseline_complete,
            None,
        ),
        #
        (
            "unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Line.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        (
            "unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Ring.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        (
            "unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Hub_Spoke.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        (
            "unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Tree.json",
            run_degree_baseline,
            nx.centrality.degree_centrality,
        ),
        # in_degree
        (
            "unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Line_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        (
            "unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Ring_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        (
            "unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Hub_Spoke_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        (
            "unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/in_degree/Tree_Directed.json",
            run_degree_baseline,
            nx.centrality.in_degree_centrality,
        ),
        # out_degree
        (
            "unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Line_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        (
            "unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Ring_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        (
            "unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Hub_Spoke_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
        (
            "unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/out_degree/Tree_Directed.json",
            run_degree_baseline,
            nx.centrality.out_degree_centrality,
        ),
    ]

    for p, out_path, fn, m in tqdm(paths, desc="Creating baselines"):
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        if "Directed" in out_path:
            g = create_graph(edges, directed=True)

            # from matplotlib import pyplot as plt
            # pos = nx.drawing.layout.kamada_kawai_layout(g)
            # nx.draw(g, pos)
            # nx.draw_networkx_labels(g, pos, {n: n for n in g.nodes})
            # plt.savefig(f"{out_path.split('/')[-1]}.png")
        else:
            g = create_graph(edges)

        res = fn(g, m)
        with open(out_path, "w") as f:
            json.dump(res, f)  # , indent=2)


if __name__ == "__main__":
    create_degree_baseline()
