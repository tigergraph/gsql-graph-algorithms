
# K Nearest Neighbors

#### [K Nearest Neighbors Changelog](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph K Nearest Neighbors Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#k-nearest-neighbors-cosine-neighbor-similarity-all-vertices-batch)

## Available K Nearest Neighbors Algorithms 

* [`movie_knn_cosine_all`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_all.gsql)

* [`movie_knn_cosine_all_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_all_file.gsql)

* [`movie_knn_cosine_ss`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_ss.gsql)

* [`movie_knn_cosine_ss_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_ss_attr.gsql)

* [`movie_knn_cosine_all_attr`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_all_attr.gsql)

* [`movie_knn_cosine_cv`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_cv.gsql)

* [`movie_knn_cosine_ss_file`](https://github.com/karimsaraipour/gsql-graph-algorithms/tree/algorithm-folder-restructure/algorithms/templates/examples/k_nearest_neighbors/movie_knn_cosine_ss_file.gsql)

## Installation 

### Replace `<K Nearest Neighbors Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <K Nearest Neighbors Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <K Nearest Neighbors Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <K Nearest Neighbors Algorithm>
```