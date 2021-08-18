
# Connected Components

#### [Connected Components Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/connected_components/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Connected Components Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#connected-components)

## Available Connected Components Algorithms 

* [`social_conn_comp_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/connected_components/social_conn_comp_attr.gsql)

* [`social_conn_comp_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/connected_components/social_conn_comp_file.gsql)

* [`social_conn_comp`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/connected_components/social_conn_comp.gsql)

## Installation 

### Replace `<Connected Components Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Connected Components Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Connected Components Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Connected Components Algorithm>
```