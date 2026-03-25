# PageRank

> **Official Documentation:** [TigerGraph PageRank Docs](https://docs.tigergraph.com/graph-ml/current/centrality-algorithms/pagerank)

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [When to Use PageRank](#when-to-use-pagerank)
- [Available Algorithms](#available-algorithms)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Parameters](#parameters)
- [Performance Notes](#performance-notes)
- [Resources](#resources)

---

## Overview

**PageRank** is a graph centrality algorithm originally developed by Google to rank web pages based on the structure of incoming links. In graph terms, it measures the relative importance of each vertex by considering both the number and quality of edges pointing to it — the underlying principle being that a vertex is more important if it is referenced by other important vertices.

This implementation is part of the [TigerGraph Graph Data Science (GDS) Library](https://github.com/tigergraph/gsql-graph-algorithms) — a collection of open-source graph algorithms written in GSQL, TigerGraph's query language.

---

## How It Works

PageRank assigns each vertex a score that is computed iteratively. At each iteration, a vertex distributes its current score equally (or proportionally, in the weighted variant) among its outgoing neighbors. The score of a vertex is updated as the sum of contributions received from all its incoming neighbors, adjusted by a **damping factor**.

The formula for a vertex `v` is:

```
PR(v) = (1 - d) + d * Σ [ PR(u) / OutDegree(u) ]
```

| Symbol | Description |
|--------|-------------|
| `PR(v)` | PageRank score of vertex `v` |
| `d` | Damping factor (typically `0.85`) — models the probability of following a link vs. jumping to a random vertex |
| `PR(u)` | PageRank score of an incoming neighbor `u` |
| `OutDegree(u)` | Number of outgoing edges from vertex `u` |

The algorithm runs for a fixed number of iterations or until scores converge below a defined threshold.

> **Key Property:** PageRank is a global algorithm — it considers the entire graph structure, not just the local neighborhood of a vertex.

---

## When to Use PageRank

PageRank is best suited for scenarios where you need to identify the most **influential or authoritative vertices** in a graph based on connectivity patterns.

**Common real-world applications include:**

- **Web & Search** — Ranking web pages by authority based on hyperlink structure.
- **Social Networks** — Identifying influential users based on follower/mention relationships.
- **Citation Analysis** — Finding the most impactful research papers in academic citation graphs.
- **Fraud Detection** — Surfacing highly connected entities in transaction networks that may indicate coordinated behavior.
- **Recommendation Systems** — Ranking items or users by structural importance to improve recommendations.
- **Knowledge Graphs** — Identifying key concepts or entities in a semantic graph.

---

## Available Algorithms

| Algorithm | Variant | Description | Source |
|-----------|---------|-------------|--------|
| `tg_pagerank` | Global — Unweighted | Standard PageRank treating all edges equally. | [tg_pagerank.gsql](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/global/unweighted/tg_pagerank.gsql) |
| `tg_pagerank_wt` | Global — Weighted | PageRank where edge weights influence score distribution. | [tg_pagerank_wt.gsql](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/global/weighted/tg_pagerank_wt.gsql) |
| `tg_pagerank_pers` | Personalized — Multi-Source | Biases scores toward a specified set of source vertices. | [tg_pagerank_pers.gsql](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/personalized/multi_source/tg_pagerank_pers.gsql) |
| `tg_pagerank_pers_ap_batch` | Personalized — All Pairs Batch | Computes personalized PageRank for all vertices in batch mode. | [tg_pagerank_pers_ap_batch.gsql](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/personalized/all_pairs/tg_pagerank_pers_ap_batch.gsql) |

### Choosing the Right Variant

- Use **`tg_pagerank`** for general-purpose importance ranking when edge weights are not available or not relevant.
- Use **`tg_pagerank_wt`** when edges carry meaningful weights (e.g., interaction frequency, transaction volume) that should influence rank distribution.
- Use **`tg_pagerank_pers`** when you want scores biased toward a specific subset of vertices — useful for personalized recommendations or context-aware ranking.
- Use **`tg_pagerank_pers_ap_batch`** when you need personalized PageRank computed for every vertex in the graph, processed efficiently in batches.

---

## Prerequisites

Before installing, ensure the following are in place:

- A running **TigerGraph instance** (v3.x or later recommended).
- A graph schema with directed or undirected edges, depending on your use case.
- For `tg_pagerank_wt`, edges must have a **numeric weight attribute**.
- Access to either the **TigerGraph CLI (`tg`)** or the **GSQL terminal**.

---

## Installation

Choose the installation method that matches your environment. Replace `<Algorithm>` with the name of the desired algorithm from the table above (e.g., `tg_pagerank`).

### Option 1 — Via TigerGraph CLI

```bash
$ tg box algos install <Algorithm>
```

**Example:**

```bash
$ tg box algos install tg_pagerank
```

---

### Option 2 — Via GSQL Terminal

1. Open the algorithm's `.gsql` source file from the links in the [Available Algorithms](#available-algorithms) section.
2. Copy the full query code.
3. In your GSQL terminal, run the following:

```gsql
GSQL > BEGIN
# Paste the algorithm code here
GSQL > END
GSQL > INSTALL QUERY <Algorithm>
```

**Example:**

```gsql
GSQL > BEGIN
# Paste contents of tg_pagerank.gsql here
GSQL > END
GSQL > INSTALL QUERY tg_pagerank
```

---

## Usage

Once installed, you can run the algorithm from the GSQL terminal or via the TigerGraph REST API.

### Running via GSQL

```gsql
RUN QUERY tg_pagerank(
  v_type,
  e_type,
  max_change,
  max_iter,
  damping,
  top_k,
  print_accum,
  result_attr,
  file_path,
  display_edges
)
```

### Running via REST API

```bash
curl -X GET "http://<host>:9000/query/<graph_name>/tg_pagerank" \
  -d '{"v_type": "Page", "e_type": "Link", "max_iter": 25}'
```

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `v_type` | `STRING` | The vertex type(s) to include in the computation. |
| `e_type` | `STRING` | The edge type(s) to traverse. |
| `max_change` | `FLOAT` | Convergence threshold — stops iteration when score changes fall below this value. |
| `max_iter` | `INT` | Maximum number of iterations to run. |
| `damping` | `FLOAT` | Damping factor `d` (default: `0.85`). Controls the probability of following an edge vs. teleporting. |
| `top_k` | `INT` | Number of top-ranked vertices to return in the output. |
| `print_accum` | `BOOL` | If `TRUE`, prints results to the console. |
| `result_attr` | `STRING` | Vertex attribute to write PageRank scores back to (optional). |
| `file_path` | `STRING` | File path to write results to (optional). |
| `display_edges` | `BOOL` | If `TRUE`, includes edges in the result for visualization. |
| `wt_attr` | `STRING` | *(Weighted variant only)* Edge attribute to use as the weight. |

> **Note:** Parameter availability may vary between algorithm variants. Always refer to the [official documentation](https://docs.tigergraph.com/graph-ml/current/centrality-algorithms/pagerank) or the individual source files for exact signatures.

---

## Performance Notes

- **Convergence vs. Fixed Iterations:** Setting a `max_change` threshold allows the algorithm to stop early once scores stabilize, which is more efficient than always running to `max_iter`. For large graphs, a threshold of `0.001` is a reasonable starting point.
- **Damping Factor:** The standard damping factor is `0.85`. Lowering it causes scores to converge faster but may reduce ranking accuracy; raising it increases sensitivity to graph structure but slows convergence.
- **Graph Size & Scalability:** PageRank is computationally intensive on very large graphs. TigerGraph's distributed architecture allows the algorithm to scale across partitions — ensure your graph is distributed appropriately for optimal performance.
- **Directed vs. Undirected Graphs:** PageRank is most meaningful on **directed graphs**, where the direction of edges implies endorsement or influence. On undirected graphs, results may be less semantically meaningful.
- **Personalized Variants:** `tg_pagerank_pers_ap_batch` is designed for high-throughput scenarios. For single-source personalized queries, `tg_pagerank_pers` is more appropriate and has lower overhead.

---

## Resources

| Resource | Link |
|----------|------|
| Official PageRank Documentation | [docs.tigergraph.com](https://docs.tigergraph.com/graph-ml/current/centrality-algorithms/pagerank) |
| Algorithm Changelog | [CHANGELOG.md](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/CHANGELOG.md) |
| Full GDS Algorithm Library | [gsql-graph-algorithms](https://github.com/tigergraph/gsql-graph-algorithms) 
| Community Forum | [community.tigergraph.com](https://community.tigergraph.com) |
| Discord | [discord.gg/vFbmPyvJJN](https://discord.gg/vFbmPyvJJN) |