
# Betweenness Centrality

#### [Betweenness Centrality Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/betweenness_centrality/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Betweenness Centrality Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#betweenness-centrality)

## Available Betweenness Centrality Algorithms 

* [`social_betweenness_cent`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/betweenness_centrality/social_betweenness_cent.gsql)

* [`social_betweenness_cent_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/betweenness_centrality/social_betweenness_cent_file.gsql)

* [`social_betweenness_cent_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/betweenness_centrality/social_betweenness_cent_attr.gsql)

## Installation 

### Replace `<Betweenness Centrality Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Betweenness Centrality Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Betweenness Centrality Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Betweenness Centrality Algorithm>
```