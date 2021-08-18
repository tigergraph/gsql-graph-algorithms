
# Pagerank

#### [Pagerank Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/Centrality/pagerank/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Pagerank Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#pagerank)

## Available Pagerank Algorithms 

* [`tg_pageRank_pers`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/Centrality/pagerank/tg_pageRank_pers.gsql)

* [`tg_pageRank_wt`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/Centrality/pagerank/tg_pageRank_wt.gsql)

* [`tg_pageRank`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/Centrality/pagerank/tg_pageRank.gsql)

## Installation 

### Replace `<Pagerank Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Pagerank Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Pagerank Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Pagerank Algorithm>
```