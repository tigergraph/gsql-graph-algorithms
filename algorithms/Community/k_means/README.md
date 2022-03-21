
# K Means

#### [K Means Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Community/k_means/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph K Means Documentation](https://docs.tigergraph.com/graph-algorithm-library/https://raw.githubusercontent.com/tigergraph/gsql-graph-algorithms/master/algorithms/schema-free/kmeans.gsql)

## Available K Means Algorithms 

* [`tg_kmeans_sub`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Community/k_means/tg_kmeans_sub.gsql)

* [`tg_kmeans`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Community/k_means/tg_kmeans.gsql)

## Installation 

### Replace `<K Means Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <K Means Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <K Means Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <K Means Algorithm>
```