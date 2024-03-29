
# Pagerank

#### [Pagerank Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Pagerank Documentation](https://docs.tigergraph.com/graph-ml/current/centrality-algorithms/pagerank)

## Available Pagerank Algorithms 

* [`tg_pagerank_wt`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/global/weighted/tg_pagerank_wt.gsql)

* [`tg_pagerank`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/global/unweighted/tg_pagerank.gsql)

* [`tg_pagerank_pers`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/personalized/multi_source/tg_pagerank_pers.gsql)

* [`tg_pagerank_pers_ap_batch`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Centrality/pagerank/personalized/all_pairs/tg_pagerank_pers_ap_batch.gsql)

## Installation 

### Replace `<Pagerank Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Pagerank Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Pagerank Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Pagerank Algorithm>
```
