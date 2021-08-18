
# Strongly Connected Components

#### [Strongly Connected Components Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/strongly_connected_components/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Strongly Connected Components Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#strongly-connected-components-1)

## Available Strongly Connected Components Algorithms 

* [`social_scc`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/strongly_connected_components/social_scc.gsql)

* [`social_scc_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/strongly_connected_components/social_scc_attr.gsql)

* [`social_scc_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/strongly_connected_components/social_scc_file.gsql)

## Installation 

### Replace `<Strongly Connected Components Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Strongly Connected Components Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Strongly Connected Components Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Strongly Connected Components Algorithm>
```