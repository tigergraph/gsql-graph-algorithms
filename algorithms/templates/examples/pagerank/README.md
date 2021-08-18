
# Pagerank

#### [Pagerank Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Pagerank Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#pagerank)

## Available Pagerank Algorithms 

* [`PR_pageRank_wt_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/PR_pageRank_wt_file.gsql)

* [`social_pageRank_pers_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank_pers_attr.gsql)

* [`social_pageRank_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank_attr.gsql)

* [`social_pageRank_wt`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank_wt.gsql)

* [`social_pageRank_pers`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank_pers.gsql)

* [`social_pageRank`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank.gsql)

* [`PR_pageRank_wt_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/PR_pageRank_wt_attr.gsql)

* [`social_pageRank_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank_file.gsql)

* [`social_pageRank_pers_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/pagerank/social_pageRank_pers_file.gsql)

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