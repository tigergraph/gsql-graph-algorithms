
# Estimated Diameter

#### [Estimated Diameter Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Path/estimated_diameter/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Estimated Diameter Documentation](https://docs.tigergraph.com/graph-algorithm-library/path/estimated-diameter)

## Available Estimated Diameter Algorithms 

* [`tg_max_BFS_depth`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Path/estimated_diameter/tg_max_BFS_depth.gsql)

* [`tg_estimate_diameter`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Path/estimated_diameter/tg_estimate_diameter.gsql)

## Installation 

### Replace `<Estimated Diameter Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Estimated Diameter Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Estimated Diameter Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Estimated Diameter Algorithm>
```