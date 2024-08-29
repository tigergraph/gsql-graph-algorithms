import csv
import json

import networkx as nx
import numpy as np
from tqdm import tqdm

from .base import Baseline
from .common import create_graph


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

    def create_baseline(self, paths):
        t = tqdm(paths, desc="Creating pagerank baselines")
        for p, out_path, fn, m in t:
            t.set_postfix_str(out_path.split("/")[-1].split(".")[0])
            with open(p) as f:
                edges = np.array(list(csv.reader(f)))

            directed = True if "Directed" in out_path else False
            weights = True if "Weighted" in out_path else False
            g = create_graph(edges, weights, directed)

            res = fn(g, m)
            with open(out_path, "w") as f:
                json.dump(res, f)  # , indent=2)

    def run(self):
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
        ]
        self.create_baseline(paths)
