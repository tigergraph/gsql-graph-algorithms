
# Minimum Spanning Tree

#### [Minimum Spanning Tree Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/minimum_spanning_tree/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Minimum Spanning Tree Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#minimum-spanning-tree-mst)

## Available Minimum Spanning Tree Algorithms 

* [`social_mst`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/minimum_spanning_tree/social_mst.gsql)

* [`social_mst_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/minimum_spanning_tree/social_mst_attr.gsql)

* [`social_mst_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/minimum_spanning_tree/social_mst_file.gsql)

## Installation 

### Replace `<Minimum Spanning Tree Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Minimum Spanning Tree Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Minimum Spanning Tree Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Minimum Spanning Tree Algorithm>
```