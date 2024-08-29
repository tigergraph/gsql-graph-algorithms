import os

import pyTigerGraph as tg
from dotenv import load_dotenv

load_dotenv()


def get_featurizer(graph_name="graph_algorithms_testing"):
    host_name = os.getenv("HOST_NAME")
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASS")
    conn = tg.TigerGraphConnection(
        host=host_name,
        username=user_name,
        password=password,
        graphname=graph_name,
    )
    if os.environ.get("USE_TKN", "true").lower() == "true":
        conn.getToken()
    f = conn.gds.featurizer()
    return f


def get_installed_queries(conn: tg.TigerGraphConnection):
    return [k.split("/")[-1].strip() for k in conn.getInstalledQueries()]
