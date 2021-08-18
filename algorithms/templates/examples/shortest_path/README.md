
# Shortest Path

#### [Shortest Path Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Shortest Path Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#single-source-shortest-path-weighted)

## Available Shortest Path Algorithms 

* [`social_shortest_ss_pos_wt`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_pos_wt.gsql)

* [`generic_shortest_ss_no_wt_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/generic_shortest_ss_no_wt_file.gsql)

* [`generic_shortest_ss_no_wt_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/generic_shortest_ss_no_wt_attr.gsql)

* [`social_shortest_ss_no_wt`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_no_wt.gsql)

* [`social_shortest_ss_any_wt_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_any_wt_attr.gsql)

* [`social_shortest_ss_any_wt`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_any_wt.gsql)

* [`social_shortest_ss_pos_wt_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_pos_wt_attr.gsql)

* [`work_shortest_sp_pos_wt`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/work_shortest_sp_pos_wt.gsql)

* [`social_shortest_ss_any_wt_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_any_wt_file.gsql)

* [`social_shortest_ss_pos_wt_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/shortest_path/social_shortest_ss_pos_wt_file.gsql)

## Installation 

### Replace `<Shortest Path Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Shortest Path Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Shortest Path Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Shortest Path Algorithm>
```