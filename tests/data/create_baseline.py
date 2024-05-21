import csv
import json

import networkx as nx
import numpy as np

baseline_path_root = "baseline/graph_algorithms_baselines"


def run_degree_baseline(g: nx.Graph):
    res = nx.centrality.degree_centrality(g)
    nx.centrality.degree_centrality

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"@@top_scores_heap": out}]
    return out


def create_graph(path, edges, weights):
    g = nx.Graph()
    # include edge weights if they exist
    if weights is not None:
        g.add_weighted_edges_from(edges)
    else:
        g.add_edges_from(edges)
    return g


def create_degree_baseline():
    # input, output
    paths = [
        (
            "unweighted_edges/complete_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/CompleteUnweighted.json",
            False,
        ),
        (
            "weighted_edges/complete_edges.csv",
            f"{baseline_path_root}/centrality/degree_centrality/CompleteWeighted.json",
            True,
        ),
    ]

    for p, o_path, w in paths:
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        g = create_graph(p, edges, w)

        res = run_degree_baseline(g)
        with open(o_path, "w") as f:
            json.dump(res, f, indent=2)


if __name__ == "__main__":
    create_degree_baseline()
