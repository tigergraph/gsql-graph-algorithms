
# Cosine

#### [Cosine Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Cosine Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#cosine-similarity-of-neighborhoods-batch)

## Available Cosine Algorithms 

* [`movie_cosine_nbor_ap_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/movie_cosine_nbor_ap_file.gsql)

* [`movie_cosine_nbor_ap`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/movie_cosine_nbor_ap.gsql)

* [`movie_cosine_nbor_ap_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/movie_cosine_nbor_ap_attr.gsql)

* [`movie_cosine_nbor_ss`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/movie_cosine_nbor_ss.gsql)

* [`movie_cosine_nbor_ss_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/movie_cosine_nbor_ss_attr.gsql)

* [`movie_cosine_nbor_ss_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/cosine/movie_cosine_nbor_ss_file.gsql)

## Installation 

### Replace `<Cosine Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Cosine Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Cosine Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Cosine Algorithm>
```