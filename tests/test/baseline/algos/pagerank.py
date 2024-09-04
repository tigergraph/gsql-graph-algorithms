import networkx as nx
import numpy as np
import pandas as pd
from pyTigerGraph.datasets import Datasets
from scipy.sparse import csc_matrix, csr, csr_matrix, spdiags
from sklearn import random_projection
from sklearn.preprocessing import normalize, scale

from .base import Baseline
from .common import create_baseline


def pr(g: nx.DiGraph, d=0.85):
    N = g.number_of_nodes()
    nodes = {n: 1 / N for n in g.nodes}

    dangling_nodes = [n for n in g.nodes if g.out_degree(n) == 0]
    max_change = 0.001
    max_diff = 9999

    print(sum(nodes.values9))
    i = 0
    # PageRank iterations
    while max_diff > max_change or i >= 25:
        max_diff = 0
        i += 1

        prev = nodes
        for n in nodes:
            # traverse
            for x in g.neighbors(n):
                pass
    return

    return nodes[35], nodes[35] / 2
    m: csr = nx.adjacency_matrix(g)
    M = m.todense()
    N = M.shape[1]
    w = np.ones(N) / N
    M_hat = d * M
    v = M_hat @ w + (1 - d)
    while np.linalg.norm(w - v) >= 1e-10:
        w = v
        v = M_hat @ w + (1 - d)
    return v


def run_pagerank(g: nx.Graph, metric):
    res = metric(g)

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"@@top_scores_heap": out}]
    return out


class PagerankBaseline(Baseline):
    def __init__(self, data_path_root, baseline_path_root):
        self.data_path_root = data_path_root
        self.baseline_path_root = baseline_path_root

    def run(self):
        ds_name = "CoraV2"
        # run pagerank on cora
        dataset = Datasets(ds_name)
        edges = pd.read_csv(dataset.tmp_dir + f"/{ds_name}/edges.csv", header=None)
        edges.columns = ["src", "tgt"]
        print(edges)

        g = nx.DiGraph()
        g.add_edges_from(edges.to_numpy())
        rank = {int(k): v for k, v in nx.pagerank(g).items()}
        rank[0] = sum(rank.values())
        rank = dict(sorted(rank.items(), key=lambda x: x[0]))
        import json

        with open("nx.json", "w") as f:
            json.dump(rank, f, indent=2)

        from matplotlib import pyplot as plt

        # pos = nx.drawing.layout.kamada_kawai_layout(g)
        # pos = nx.drawing.layout.arf_layout(g)
        # nx.draw(g, pos)
        # nx.draw_networkx_labels(g, pos, {n: n for n in g.nodes})
        # plt.savefig(f"{out_path.split('/')[-1]}.png")
        # plt.show()
        # custom pagerank
        print(pr(g))
        return
        # (data, output_path, fun, metric)
        paths = [
            (
                f"{self.data_path_root}/unweighted_edges/complete_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Complete.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Line.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Ring.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Hub_Spoke.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Tree.json",
                run_pagerank,
                nx.pagerank,
            ),
            # directed
            (
                f"{self.data_path_root}/unweighted_edges/line_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Line_Directed.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/ring_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Ring_Directed.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/hubspoke_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Hub_Spoke_Directed.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/tree_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Tree_Directed.json",
                run_pagerank,
                nx.pagerank,
            ),
            (
                f"{self.data_path_root}/unweighted_edges/empty_graph_edges.csv",
                f"{self.baseline_path_root}/centrality/pagerank/Empty.json",
                run_pagerank,
                nx.pagerank,
            ),
        ]
        create_baseline(paths, algo="pagerank")
