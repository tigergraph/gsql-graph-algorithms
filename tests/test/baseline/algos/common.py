import csv
import json

import networkx as nx
import numpy as np
from tqdm import tqdm


def create_graph(edges, weights=False, directed=False) -> nx.Graph:
    if directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    if weights:
        # make weights floats
        edges = [[a, b, float(c)] for a, b, c in edges]
        g.add_weighted_edges_from(edges)
    else:
        g.add_edges_from(edges)
    return g


def create_baseline(paths, algo):
    t = tqdm(paths, desc=f"Creating {algo} baselines")
    for p, out_path, fn, m in t:
        t.set_postfix_str(out_path.split("/")[-1].split(".")[0])
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        directed = True if "Directed" in out_path else False
        weights = True if "Weighted" in out_path else False
        g = create_graph(edges, weights, directed)

            # from matplotlib import pyplot as plt
            # pos = nx.drawing.layout.kamada_kawai_layout(g)
            # nx.draw(g, pos)
            # nx.draw_networkx_labels(g, pos, {n: n for n in g.nodes})
            # plt.savefig(f"{out_path.split('/')[-1]}.png")

        res = fn(g, m)
        with open(out_path, "w") as f:
            json.dump(res, f)  # , indent=2)
