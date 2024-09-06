import networkx as nx
import pandas as pd
from pyTigerGraph.datasets import Datasets

from .base import Baseline
from .common import create_baseline


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
        return
