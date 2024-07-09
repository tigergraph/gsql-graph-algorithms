import gzip
import json

import networkx as nx
import numpy as np
import pandas as pd
from algos import fastrp
from dotenv import load_dotenv
from pyTigerGraph.datasets import Datasets

load_dotenv()
data_path_root = "data"
baseline_path_root = f"{data_path_root}/baseline"


def run(ds_name="Cora"):
    dataset = Datasets(ds_name)
    edges = pd.read_csv(dataset.tmp_dir + f"/{ds_name}/edges.csv", header=None)
    edges.columns = ["src", "tgt"]

    g = nx.Graph()
    g.add_edges_from(edges.to_numpy())
    node_ids = sorted(list(g.nodes))
    A = nx.adjacency_matrix(g, nodelist=node_ids)
    conf = {
        "weights": [1, 2, 4],
        "dim": 8,
        # "projection_method": "sparse",
        "projection_method": "gaussian",
        "input_matrix": "trans",
        "alpha": -0.628,
        "normalization": False,
    }

    vecs = fastrp(A, conf)

    assert len(vecs) == len(node_ids)

    res = {str(k): list(v) for k, v in zip(node_ids, vecs)}
    with gzip.open(f"{baseline_path_root}/ml/fastRP.json.gz", "wb") as f:
        f.write(json.dumps(res).encode())

    with gzip.open(f"{baseline_path_root}/ml/fastRP.json.gz", "rb") as f:
        d = json.load(f)
