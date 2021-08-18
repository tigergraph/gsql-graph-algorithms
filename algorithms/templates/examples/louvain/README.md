
# Louvain

#### [Louvain Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/louvain/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Louvain Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#louvain-method-with-parallelism-and-refinement)

## Available Louvain Algorithms 

* [`social_louvain_parallel_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/louvain/social_louvain_parallel_attr.gsql)

* [`social_louvain_parallel_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/louvain/social_louvain_parallel_file.gsql)

* [`social_louvain_parallel`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/louvain/social_louvain_parallel.gsql)

## Installation 

### Replace `<Louvain Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Louvain Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Louvain Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Louvain Algorithm>
```