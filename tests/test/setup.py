import json
import os
import re
import time
from glob import glob

import pyTigerGraph as tg
from dotenv import load_dotenv
from pyTigerGraph.datasets import Datasets
from tqdm import tqdm, trange

import util

load_dotenv()
graph_name = "graph_algorithms_testing"
pattern = re.compile(r'"name":\s*"tg_.*"')


# def add_reverse_edge(ds: Datasets):
#     with open(f"{dataset.tmp_dir}/{ds.name}/create_schema.gsql") as f:
#         schema: str = f.read()
#     with open(f"{dataset.tmp_dir}/{ds.name}/create_schema.gsql", "w") as f:
#         schema = schema.replace(
#             "ADD DIRECTED EDGE Cite (from Paper, to Paper, time Int, is_train Bool, is_val Bool);",
#             'ADD DIRECTED EDGE Cite (from Paper, to Paper, time Int, is_train Bool, is_val Bool) WITH REVERSE_EDGE="reverse_Cite";',
#         )
#         f.write(schema)
#
#
def get_query_path(q_name):
    pth = glob(f"../algorithms/**/{q_name}.gsql", recursive=True)
    return pth[0]


if __name__ == "__main__":
    host_name = os.environ["HOST_NAME"]
    user_name = os.environ["USER_NAME"]
    password = os.environ["PASS"]
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
    # dataset = Datasets("Cora")
    # add_reverse_edge(dataset)
    # conn.ingestDataset(dataset, getToken=True)

    # dataset = Datasets("graph_algorithms_testing")
    # conn.ingestDataset(dataset, getToken=True)
    conn.getToken()

    conn.graphname = graph_name
    # install the queries
    feat = conn.gds.featurizer()  # type: ignore
    installed_queries = util.get_installed_queries(conn)
    algos = json.dumps(feat.algo_dict, indent=1)
    queries = [
        m.split(": ")[1].replace('"', "").strip() for m in pattern.findall(algos)
    ]

    t = tqdm(queries, desc="installing GDS queries")
    for q in t:
        t.set_postfix({"query": q})
        pth = get_query_path(q)
        if q not in installed_queries:
            feat.installAlgorithm(q, pth)

    # for _ in trange(30, desc="Sleeping while data loads"):
        # time.sleep(1)
