import json
import os
import re

import pyTigerGraph as tg
import util
from dotenv import load_dotenv
from pyTigerGraph.datasets import Datasets
from tqdm import tqdm

load_dotenv()
graph_name = "graph_algorithms_testing"
DEV = os.getenv("DEV", "false").lower() == "true"
pattern = re.compile(r'"name":\s*"tg_.*"')

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
    dataset = Datasets("graph_algorithms_testing")
    conn.ingestDataset(dataset, getToken=True)

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

