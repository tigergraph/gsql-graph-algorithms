import csv
import json

import networkx as nx
import numpy as np
from algos import run_pagerank_baseline, tg_pagerank, tg_pagerank_wt
from tqdm import tqdm

data_path_root = "data/"
baseline_path_root = f"{data_path_root}/baseline/"


def create_graph(edges, weights=False, directed=False):
    if directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    if weights:
        edges = [[a, b, float(c)] for a, b, c in edges]
        g.add_weighted_edges_from(edges)
    else:
        g.add_edges_from(edges)
    return g


def create_pagerank_baseline(paths):
    t = tqdm(paths, desc="Creating PageRank baselines")
    for p, out_path, fn, m in t:
        t.set_postfix_str(out_path.split("/")[-1].split(".")[0])
        with open(p) as f:
            edges = np.array(list(csv.reader(f)))

        directed = True if "Directed" in out_path else False
        weights = True if "Weighted" in out_path else False
        g = create_graph(edges, weights, directed)

        res = fn(g, m)
        print(out_path.split("/")[-1].split(".")[0])
        print(res)
        # with open(out_path, "w") as f:
        #     json.dump(res, f)


def run():
    # (data, output_path, fn, metric)
    paths = [
        # ── PageRank (unweighted, undirected) ─────────────────────────────────
        (
            f"{data_path_root}/unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Line.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        (
            f"{data_path_root}/unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Ring.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        (
            f"{data_path_root}/unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Hub_Spoke.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        (
            f"{data_path_root}/unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Tree.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        # ── PageRank (unweighted, directed) ───────────────────────────────────
        (
            f"{data_path_root}/unweighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Line_Directed.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        (
            f"{data_path_root}/unweighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Ring_Directed.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        (
            f"{data_path_root}/unweighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Hub_Spoke_Directed.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        (
            f"{data_path_root}/unweighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/pagerank/Tree_Directed.json",
            run_pagerank_baseline,
            tg_pagerank,
        ),
        # ── Weighted PageRank ──────────────────────────────────────────────────
        (
            f"{data_path_root}/weighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Line_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        (
            f"{data_path_root}/weighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Ring_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        (
            f"{data_path_root}/weighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Hub_Spoke_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        (
            f"{data_path_root}/weighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Tree_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        # ── Weighted PageRank (directed) ───────────────────────────────────────
        (
            f"{data_path_root}/weighted_edges/line_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Line_Directed_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        (
            f"{data_path_root}/weighted_edges/ring_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Ring_Directed_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        (
            f"{data_path_root}/weighted_edges/hubspoke_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Hub_Spoke_Directed_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
        (
            f"{data_path_root}/weighted_edges/tree_edges.csv",
            f"{baseline_path_root}/centrality/pagerank_wt/Tree_Directed_Weighted.json",
            run_pagerank_baseline,
            tg_pagerank_wt,
        ),
    ]
    create_pagerank_baseline(paths)


if __name__ == "__main__":
    run()