
# Cycle Detection

#### [Cycle Detection Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cycle_detection/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Cycle Detection Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#cycle-detection)

## Available Cycle Detection Algorithms 

* [`social_cycle_detection`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cycle_detection/social_cycle_detection.gsql)

* [`social_cycle_detection_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cycle_detection/social_cycle_detection_file.gsql)

## Installation 

### Replace `<Cycle Detection Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Cycle Detection Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Cycle Detection Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Cycle Detection Algorithm>
```