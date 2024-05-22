import csv
import json

import networkx as nx
import numpy as np
from tqdm import tqdm

baseline_path_root = "baseline"


def run_degree_baseline_complete(g: nx.Graph):
    s = 1.0 / (len(g) - 1.0)

    # d-1 because nx will double count the self-edge
    res = {n: (d - 1) * s for n, d in g.degree()}

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def run_degree_baseline(g: nx.Graph):
    res = nx.centrality.degree_centrality(g)

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def create_graph(edges, weights=False):
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
        ),
        (
            "unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Line.json",
            run_degree_baseline,
        ),
        (
            "unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Ring.json",
            run_degree_baseline,
        ),
        (
            "unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Hub_Spoke.json",
            run_degree_baseline,
        ),
        (
            "unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/Tree.json",
            run_degree_baseline,
        ),
        # do the following directed edges
        # "Line_Directed",
        # "Ring_Directed",
        # "Hub_Spoke_Directed",
        # "Tree_Directed",
        # (
        #     "unweighted_edges/tree_edges.csv",
        #     f"{baseline_path_root}/centrality/degree_centrality/Tree.json",
        #     run_degree_baseline,
        # ),
    ]

    for p, out_path, fn in tqdm(paths):
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        g = create_graph(edges)

        res = fn(g)
        with open(out_path, "w") as f:
            json.dump(res, f)  # , indent=2)


if __name__ == "__main__":
    create_degree_baseline()
