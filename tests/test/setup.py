import json
import os
import re
from glob import glob

import pyTigerGraph as tg
from dotenv import load_dotenv
from pyTigerGraph.datasets import Datasets
from tqdm import tqdm

import util
from baseline import create_baselines

load_dotenv()
graph_name = "graph_algorithms_testing"
pattern = re.compile(r'"name":\s*"tg_.*"')


def get_query_path(q_name):
    pth = glob(f"../algorithms/**/{q_name}.gsql", recursive=True)
    return pth[0]


def get_template_queries() -> list[str]:
    paths = []
    packages = []
    for p in glob(f"../GDBMS_ALGO/**/*.gsql", recursive=True):
        name = p.replace("../", "").split(".")[0].split("/")
        pkg = ".".join(x for x in name[:-1])
        name = ".".join(x for x in name)
        paths.append((name, p))
        packages.append(pkg)

    packages = set(packages)
    return packages, paths


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
    res = conn.ping()
    print(f"ping: {res}")
    if res["error"]:
        exit(1)

    # load the data
    dataset = Datasets("CoraV2")
    # add_reverse_edge(dataset)
    conn.ingestDataset(dataset, getToken=True)

    dataset = Datasets("graph_algorithms_testing")
    conn.ingestDataset(dataset, getToken=True)

    if os.environ.get("USE_TKN", "true").lower() == "true":
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

    # install template queries
    print(conn.gsql("DROP PACKAGE GDBMS_ALGO"))
    print(conn.gsql("CREATE PACKAGE GDBMS_ALGO"))
    packages, queries = get_template_queries()
    for p in packages:
        print(conn.gsql(f"CREATE PACKAGE {p}"))

    t = tqdm(queries, desc="installing Template queries")
    for q, pth in t:
        t.set_postfix({"query": q})
        with open(pth) as f:
            query = f.read()
        conn.gsql(f"{query}")

    pkg_queries = []
    queries = [q[0] for q in queries]
    reg = re.compile(r"- (.*)\(.*\)")  # find installed pacakge query names
    for pkg in packages:
        r = conn.gsql(f"SHOW PACKAGE {pkg}")
        for p in reg.findall(r):
            p = f"{pkg}.{p}"
            pkg_queries.append(p)

    # TODO:
    # check that all the template queries were installed
    # for q in queries:
    #     print(q, q in pkg_queries)

    create_baselines.run()
