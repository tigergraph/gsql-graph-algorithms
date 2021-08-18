
# Closeness

#### [Closeness Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/closeness/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Closeness Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#closeness-centrality)

## Available Closeness Algorithms 

* [`social_closeness_cent_tmp`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/closeness/social_closeness_cent_tmp.gsql)

* [`social_closeness_cent_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/closeness/social_closeness_cent_attr.gsql)

* [`social_closeness_cent_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/closeness/social_closeness_cent_file.gsql)

* [`social_closeness_cent`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/closeness/social_closeness_cent.gsql)

## Installation 

### Replace `<Closeness Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Closeness Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Closeness Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Closeness Algorithm>
```