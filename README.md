# GSQL Algorithm Library
For TigerGraph version 3.1 or higher
9/3/21

The GSQL Graph Algorithm Library is a collection of high-performance GSQL queries,
each of which implements a standard graph algorithm. Each algorithm is ready to be
installed and used, either as a stand-alone query or as a building block of a larger
analytics application.GSQL running on the TigerGraph platform is particularly
well-suited for graph algorithms:

* Turing-complete with full support for imperative and procedural programming,
 ideal for algorithmic computation.

* Parallel and Distributed Processing, enabling computations on larger graphs.

* User-Extensible.
  Because the algorithms are written in standard GSQL and compiled by the user,
  they are easy to modify and customize.

* Open-Source. Users can study the GSQL implementations to learn by
  example, and they can develop and submit additions to the library.

## Library Structure

You can download the library from github:
https://github.com/tigergraph/gsql-graph-algorithms

The library contains e main sections: algorithms and graphs, and UDF.

The algorithms folder has two levels of subfolders to categorize by category and algorithm.
Within each algorithm folder is 1 or more algorithm queries, a README and a CHANGELOG file.
If any subqueries, UDF (user-defined function), or other auxiliary files are needed, they
are also there.
		
The graphs folder contains small sample graphs that you can use to experiment with the
algorithms. In our online documentation, we use the test graphs to show you the expected
result for each algorithm. The graphs are small enough that you can manually calculate
and sometimes intuitively see what the answers should be.

The UDF folder contains an ExprFunctions.hpp file which contains custom C++ functons which
extend the GSQL query language and are needed by certain algorithms.
## NOTES:
1. Currently, each TigerGraph installation has one global ExprFunctions.hpp which must contain
the UDFs for all queries.  Therefore, the ExprFunctions.hpp file(s) you find here need to be merged
with the global ExprFunctions.hpp.  Section docs.tigergraph.com for more information about
Installing User-Defined Functions with the GET and PUT commands.
2. This central UDF folder is a legacy feature for older algorithms. For newer algorithms,
the UDF files are located in their individual subfolders.


## Table of GSQL Graph Algorithms
As of October 5, 2021

| Query name                 | Description                                                             |
|----------------------------|-------------------------------------------------------------------------|
| `tg_adamic_adar`           | Adamic Adar Topoligical Link Prediction
| `tg_article_rank`          | Article rank                                                            |
| `tg_astar`                 | A* search                                                               |
| `tg_betweenness_cent`      | Betweenness centrality                                                  |
| `tg_bfs`                   | Breadth-first search                                                    |
| `tg_closeness_cent_approx` | Approximate closeness centrality                                        |
| `tg_closeness_cent`        | Closeness centrality                                                    |
| `tg_common_neighbors`      | Common neighbors topological link prediction                            |
| `tg_cosine_batch`          | Cosine similarity for each pair of vertices, computed in batches        |
| `tg_cosine_nbor_ap`        | Cosine similarity for each pair of vertices                             |
| `tg_cosine_nbor_ss`        | Cosine similarity from a single vertex                                  |
| `tg_cycle_detection`       | Rocha–Thatte algorithm for cycle detection; output the cycles           |
| `tg_cycle_detection_count` | Rocha–Thatte algorithm for cycle detection; output the number of cycles |
| `tg_degree_cent`           | Degree centrality                                                       |
| `tg_eigenvector_cent`      | Eigenvector centrality                                                  |
| `tg_embedding_cosine_sim`  | One-to-Many embedding cosine similarity                                 |
| `tg_embedding_pairwise_cosine_sim` | Pairwise embedding cosine similarity                            |
| `tg_estimate_diameter`     | Heuristic estimate of graph diameter                                    |
| `tg_fastRP`                | FastRP graph embedding                                                  |
| `tg_greedy_graph_coloring` | Greedy graph coloring                                                   |
| `tg_harmonic_cent`         | Harmonic centraliity                                                    |
| `tg_influence_maximization_CELF` | Influence maximization using CELF                                 |
| `tg_influence_maximization_greedy` | Influence maximization using greedy method                      |
| `tg_jaccard_batch`         | Jaccard similarity for each pair of vertices, computed in batches       |
| `tg_jaccard_nbor_ap` [1]   | Jaccard similarity for each pair of vertices                            |
| `tg_jaccard_nbor_ss` [1]   | Jaccard similarity from a single vertex                                 |
| `tg_kcore`                 | K-Core                                                                  |
| `tg_kmeans`                | K-Means                                                                 |
| `tg_knn_cosine_all`        | k-Nearest Neighbor classification, using cosine similarity, batch       |
| `tg_knn_cosine_cv`         | Cross validation for k-Nearest Neighbor, using cosine similarity        |
| `tg_knn_cosine_ss`         | k-Nearest Neighbor classification, using cosine sim., single source     |
| `tg_label_prop`            | Label propagation method for community detection                        |
| `tg_lcc`                   | Local clustering coefficient                                            |
| `tg_louvain_distributed`   | Distributed & parallel Louvain Modularity optimzation                   |
| `tg_louvain_parallel`      | Parallel Louvain Modularity optimization                                |
| `tg_maxflow`               | Maxflow                                                                 |
| `tg_maximal_indep_set`     | Maximal independent set                                                 |
| `tg_msf`                   | Minimum spanning forest (MSF)                                           |
| `tg_mst`                   | Minimum spanning tree (MST)                                             |
| `tg_node2vec`              | node2vec graph embedding                                                |
| `tg_pagerank_pers` [1]     | Personalized PageRank                                                   |
| `tg_pagerank_wt` [1]       | Weighted PageRank                                                       |
| `tg_pagerank` [1]          | PageRank measurement of relative influence of each vertex               |
| `tg_preferential_attachment` | Preferential attachment topological link prediction                   |
| `tg_random_walk`           | Random walk generator                                                   |
| `tg_random_walk_batch`     | Random walk generator, in batches for greater memory efficiency         |
| `tg_resource_allocation`   | Resource allocation topological link prediction                         |
| `tg_same_community`        | Same community topological link prediction                              |
| `tg_scc`                   | Strongly connected component detection                                  |
| `tg_scc_small_world`       | Strongly connected component detection                                  |
| `tg_shortest_ss_any_wt`    | Single-Source shortest paths                                            |
| `tg_shortest_ss_no_wt`     | Single-Source shortest paths without weight                             |
| `tg_shortest_ss_pos_wt`    | Single-Source shortest paths with positive weight                       |
| `tg_slpa`                  | Speaker-Listener Label Propagation                                      |
| `tg_tri_count_fast`        | Count all the triangles, faster but using more memory                   |
| `tg_tri_count`             | Count all the triangles, memory effient                                 |
| `tg_total_neighbors`       | Total neighbors topological link prediction                             |
| `tg_wcc`                   | Weakly (undirect) Connected component detection                         |
| `tg_wcc_small_world`       | Weakly (undirect) Connected component detection                         |
| `tg_weighted_random_walk`  | Weighted random walk generator                                          |
| `tg_weighted_random_walk_batch` | Weighted random walk generator, in batches for greater memory efficiency |
Notes:
[1] The schema-free version of this algorithm can use only one edge type.


The schema-free algorithms ofter all three options in one algorithm.

## Get Started

If you want to use one of the test graphs, load it before installing the algorithms:
See the README.test file in the tests folder
   
* Schema-free algorithms:
  1. Change the graph name specified in CREATE statement.
  2. Use the script directly.

More detailed documentation and examples are available on the web at
https://docs.tigergraph.com/graph-algorithm-library
