import json
import os
import re
import time

import pyTigerGraph as tg
from dotenv import load_dotenv
from pyTigerGraph.datasets import Datasets
from tqdm import tqdm, trange

import util

load_dotenv()
graph_name = "graph_algorithms_testing"
pattern = re.compile(r'"name":\s*"tg_.*"')


def add_reverse_edge(ds: Datasets):
    with open(f"{dataset.tmp_dir}/{ds.name}/create_schema.gsql") as f:
        schema: str = f.read()
    with open(f"{dataset.tmp_dir}/{ds.name}/create_schema.gsql", "w") as f:
        schema = schema.replace(
            "ADD DIRECTED EDGE Cite (from Paper, to Paper, time Int, is_train Bool, is_val Bool);",
            'ADD DIRECTED EDGE Cite (from Paper, to Paper, time Int, is_train Bool, is_val Bool) WITH REVERSE_EDGE="reverse_Cite";',
        )
        f.write(schema)


if __name__ == "__main__":
    host_name = os.getenv("HOST_NAME")
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASS")
    conn = tg.TigerGraphConnection(
        host=host_name,
        username=user_name,
        password=password,
        graphname=graph_name,
    )
    print("checking ping")
    res = conn.ping()
    print(res)
    if res["error"]:
        exit(1)
    # load the data
    dataset = Datasets("Cora")
    add_reverse_edge(dataset)
    conn.ingestDataset(dataset, getToken=True)

    dataset = Datasets("graph_algorithms_testing")
    conn.ingestDataset(dataset, getToken=True)

    conn.graphname = graph_name
    # install the queries
    feat = conn.gds.featurizer()
    installed_queries = util.get_installed_queries(conn)
    algos = json.dumps(feat.algo_dict, indent=1)
    queries = [
        m.split(": ")[1].replace('"', "").strip() for m in pattern.findall(algos)
    ]
    for q in tqdm(queries, desc="installing GDS queries"):
        if q not in installed_queries:
            print(q)
            feat.installAlgorithm(q)

    for _ in trange(30, desc="Sleeping while data loads"):
        time.sleep(1)
