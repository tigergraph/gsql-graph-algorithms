# Preferential Attachment

#### [Preferential Attachment Changelog](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/LinkPrediction/adamic_adair/CHANGELOG.md) | [Discord](https://discord.gg/vFbmPyvJJN) | [Community](https://community.tigergraph.com) | [TigerGraph Starter Kits](https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser)

## [TigerGraph Preferential Attachment Documentation](https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#preferential-attachment)

## Available Preferential Attachment Algorithms

* [`tg_preferential_attachment`](https://github.com/tigergraph/gsql-graph-algorithms/blob/master/algorithms/LinkPrediction/preferential_attachment/tg_preferential_attachment.gsql)

## Installation 

### Replace `<Preferential Attachment>` with desired algorithm listed above 

#### Via TigerGraph CLI

```bash
$ tg box algos install <Preferential Attachment>
```

#### Via GSQL terminal

```bash
GSQL > BEGIN
# Paste <Preferential Attachment> code after BEGIN command
GSQL > END 
GSQL > INSTALL QUERY <Preferential Attachment>
```