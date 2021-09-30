# Same Community

#### [Same Community Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/LinkPrediction/same_community/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Same Community Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#common-neighbors)

## Available Same Community Algorithms

* [`tg_same_community`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/LinkPrediction/same_community/tg_same_community.gsql)

## Installation 
Assumes that you already have used a community finding algorithm, with results stored as attributes on your vertices.

### Replace `<Same Community>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Same Community>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Same Community> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Same Community>
```