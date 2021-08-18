
# Jaccard

#### [Jaccard Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Jaccard Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#jaccard-similarity-of-neighborhoods-batch)

## Available Jaccard Algorithms 

* [`movie_jaccard_nbor_ap_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/movie_jaccard_nbor_ap_file.gsql)

* [`movie_jaccard_nbor_ss_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/movie_jaccard_nbor_ss_file.gsql)

* [`movie_jaccard_nbor_ss`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/movie_jaccard_nbor_ss.gsql)

* [`movie_jaccard_nbor_ss_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/movie_jaccard_nbor_ss_attr.gsql)

* [`movie_jaccard_nbor_ap`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/movie_jaccard_nbor_ap.gsql)

* [`movie_jaccard_nbor_ap_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/jaccard/movie_jaccard_nbor_ap_attr.gsql)

## Installation 

### Replace `<Jaccard Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Jaccard Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Jaccard Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Jaccard Algorithm>
```