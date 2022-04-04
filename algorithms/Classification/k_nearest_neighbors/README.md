
# K Nearest Neighbors

#### [K Nearest Neighbors Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Similarity/nearest_neighbors/k_nearest_neighbors/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph K Nearest Neighbors Documentation](https://docs.tigergraph.com/graph-ml/current/classification-algorithms/k-nearest-neighbors)

## Available K Nearest Neighbors Algorithms 

* [`tg_knn_cosine_cv`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Classification/k_nearest_neighbors/cross_validation/tg_knn_cosine_cv.gsql)

* [`tg_knn_cosine_cv_sub`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Classification/k_nearest_neighbors/cross_validation/tg_knn_cosine_cv_sub.gsql)

* [`tg_knn_cosine_all`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Classification/k_nearest_neighbors/all_pairs/tg_knn_cosine_all.gsql)

* [`tg_knn_cosine_all_sub`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Classification/k_nearest_neighbors/all_pairs/tg_knn_cosine_all_sub.gsql)

* [`tg_knn_cosine_ss`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Classification/k_nearest_neighbors/single_source/tg_knn_cosine_ss.gsql)

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
