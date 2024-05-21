import csv
import json

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

baseline_path_root = "baseline/graph_algorithms_baselines"


def run_degree_baseline(g: nx.Graph):
    # res = nx.centrality.degree_centrality(g)
    s = 1.0 / (len(g) - 1.0)
    res = {n: (d-1) * s for n, d in g.degree()} # d-1 because nx will double count the self-edge

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def create_graph(edges, weights):
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
            False,
        ),
        # (
        #     "weighted_edges/complete_edges.csv",
        #     f"{baseline_path_root}/centrality/weighted_degree_centrality/CompleteWeighted.json",
        #     True,
        # ),
    ]

    for p, o_path, w in paths:
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        g = create_graph(edges, w)

        res = run_degree_baseline(g)
        with open(o_path, "w") as f:
            json.dump(res, f, indent=2)


if __name__ == "__main__":
    create_degree_baseline()
