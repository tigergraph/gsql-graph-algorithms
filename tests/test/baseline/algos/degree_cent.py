from collections import Counter

import networkx as nx


def run_degree_baseline_complete(g: nx.Graph, _):
    s = 1.0 / (len(g) - 1.0)

    # d-1 because nx will double count the self-edge
    res = {n: (d - 1) * s for n, d in g.degree()}

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def run_degree_baseline(g: nx.Graph, metric):
    res = metric(g)

    out = []
    for k, v in res.items():
        out.append({"Vertex_ID": k, "score": v})

    out = [{"top_scores": out}]
    return out


def weighted_deg_cent(
    g: nx.Graph,
    dir: str = "",
):
    res = Counter()
    for e in g.edges:
        a = g.get_edge_data(e[0], e[1])["weight"]
        match dir:
            case "in":
                res[e[1]] += a
            case "out":
                res[e[0]] += a
            case _:
                res[e[0]] += a
                res[e[1]] += a
    return res
