
# Cosine

#### [Cosine Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Similarity/cosine/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Cosine Documentation](https://docs.tigergraph.com/graph-ml/current/similarity-algorithms/cosine-similarity-of-neighborhoods-single-source)

## Available Cosine Algorithms 

* [`tg_cosine_nbor_ap_batch`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Similarity/cosine/all_pairs/tg_cosine_nbor_ap_batch.gsql)

* [`tg_cosine_nbor_ss`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/Similarity/cosine/single_source/tg_cosine_nbor_ss.gsql)

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
