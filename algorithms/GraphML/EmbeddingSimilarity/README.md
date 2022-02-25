
# Embeddingsimilarity

#### [Embeddingsimilarity Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/GraphML/Embeddings/EmbeddingSimilarity/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Embeddingsimilarity Documentation](https://docs.tigergraph.com/graph-ml/current/node-embeddings/)

## Available Embeddingsimilarity Algorithms 

* [`tg_embedding_pairwise_cosine_sim`](https://github.com/tigergraph/gsql-graph-algorithms/blob/github_link_fix/algorithms/GraphML/EmbeddingSimilarity/tg_embedding_pairwise_cosine_sim.gsql)

* [`tg_embedding_cosine_similarity`](https://github.com/tigergraph/gsql-graph-algorithms/blob/github_link_fix/algorithms/GraphML/EmbeddingSimilarity/tg_embedding_cosine_sim.gsql)

## Installation 

### Replace `<Embeddingsimilarity Algorithm>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Embeddingsimilarity Algorithm>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Embeddingsimilarity Algorithm> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Embeddingsimilarity Algorithm>
```
