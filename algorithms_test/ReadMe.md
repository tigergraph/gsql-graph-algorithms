# Setup
```
algorithms_test (ALGOS-263) $ ./2_setup.sh
======================================== MyGraph ========================================
Dropping the graph MyGraph...
Successfully dropped jobs on the graph 'MyGraph': [loading_job].
All jobs on the graph 'MyGraph' are dropped.
Successfully dropped queries on the graph 'MyGraph': [tg_wcc, tg_shortest_ss_any_wt, tg_pagerank_pers_ap_batch, tg_tri_count_fast, tg_louvain, tg_shortest_ss_no_wt, tg_mst, tg_scc_small_world, tg_scc, tg_embedding_pairwise_cosine_similarity, tg_all_path, tg_tri_count, tg_all_path_bidirection, tg_knn_cosine_all, tg_fpm_pre, tg_common_neighbors, tg_maximal_indep_set, tg_eigenvector_cent, tg_pagerank_pers, tg_embedding_cosine_similarity, tg_pagerank_wt, tg_harmonic_cent, tg_bfs, tg_closeness_cent_approx, tg_astar, tg_degree_cent, tg_maximal_indep_set_random, tg_wcc_small_world, tg_greedy_graph_coloring, tg_betweenness_cent, tg_resource_allocation, tg_fastRP, tg_jaccard_nbor_ap_batch, tg_knn_cosine_cv_sub, tg_kmeans_sub, tg_influence_maximization_greedy, tg_max_BFS_depth, tg_lcc, tg_closeness_cent, tg_slpa, tg_adamic_adar, tg_cosine_nbor_ss, tg_cosine_nbor_ap_batch, tg_total_neighbors, tg_knn_cosine_all_sub, tg_same_community, tg_pagerank, tg_fpm, tg_kmeans, tg_map_equation, tg_estimate_diameter, tg_cycle_detection, tg_cycle_detection_batch, tg_knn_cosine_cv, tg_kcore, tg_article_rank, tg_weisfeiler_lehman, tg_jaccard_nbor_ss, tg_maxflow, tg_cycle_component, tg_weighted_degree_cent, tg_shortest_ss_pos_wt, tg_label_prop, tg_knn_cosine_ss, tg_shortest_ss_pos_wt_tb, tg_cycle_detection_count, tg_preferential_attachment, tg_msf, tg_influence_maximization_CELF, tmp1].
All queries on the graph 'MyGraph' are dropped.
The graph MyGraph is dropped.
Finished dropping graph MyGraph.
--------------------------------------------------------------------------------
Running: Creating schema /home/tigergraph/gsql-graph-algorithms/algorithms_test/gsql/MyGraph/1_create_schema.gsql
The graph MyGraph is created.
Successfully created schema change jobs: [change_schema_of_MyGraph].
WARNING: When modifying the graph schema, reinstalling all affected queries is required, and the duration of this process may vary based on the number and complexity of the queries. To skip query reinstallation, you can run with the '-N' option, but manual reinstallation of queries will be necessary afterwards.
Kick off schema change job change_schema_of_MyGraph
Doing schema change on graph 'MyGraph' (current version: 0)
Trying to add local vertex 'MyNode' to the graph 'MyGraph'.
Trying to add local edge 'MyEdge' and its reverse edge 'rev_MyEdge' to the graph 'MyGraph'.

Graph MyGraph updated to new version 1
The job change_schema_of_MyGraph completes in 0.900 seconds!
Local schema change succeeded.
Successfully dropped jobs on the graph 'MyGraph': [change_schema_of_MyGraph].
--------------------------------------------------------------------------------
Running: Creating loading job /home/tigergraph/gsql-graph-algorithms/algorithms_test/gsql/MyGraph/2_create_loading_job.gsql
Using graph 'MyGraph'
Successfully created loading jobs: [loading_job].
--------------------------------------------------------------------------------
Running loading job for /home/tigergraph/data/public/zhishi-all/out.zhishi-all...
[Tip: Use "CTRL + C" to stop displaying the loading status update, then use "SHOW LOADING STATUS <jobid>" to track the loading progress again]
[Tip: Manage loading jobs with "ABORT/RESUME LOADING JOB <jobid>"]
Running the following loading job:
  Job name: loading_job
  Jobid: MyGraph.loading_job.file.m1.1720513082456
  Log directory: /home/tigergraph/tigergraph/log/fileLoader/MyGraph.loading_job.file.m1.1720513082456
Job "MyGraph.loading_job.file.m1.1720513082456" loading status
Current timestamp is 2024-07-09 08:19:08.627
Loading status was last updated at 2024-07-09 08:19:07.896.
[FINISHED] m1 ( Finished: 1 / Total: 1 )
  +-----------------------------------------------------------------------------------------------------+
  |                 FILENAME |    LINES |   OBJECTS |   ERRORS |   AVG SPEED |   DURATION |   PERCENTAGE|
  |zhishi-all/out.zhishi-all | 65905159 | 197715477 |        0 |   1014 kl/s |    64.97 s |        100 %|
  +-----------------------------------------------------------------------------------------------------+
LOAD SUCCESSFUL for loading jobid: MyGraph.loading_job.file.m1.1720513082456
  Job ID: MyGraph.loading_job.file.m1.1720513082456-----------------------------------------------------+
  Elapsed time: 65 sec
  Log directory: /home/tigergraph/tigergraph/log/fileLoader/MyGraph.loading_job.file.m1.1720513082456
  Summary: /home/tigergraph/tigergraph/log/fileLoader/MyGraph.loading_job.file.m1.1720513082456/summary

Finished running loading job for /home/tigergraph/data/public/zhishi-all/out.zhishi-all.
--------------------------------------------------------------------------------
All queries are dropped.
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Similarity/jaccard/all_pairs/tg_jaccard_nbor_ap_batch.gsql
Successfully created queries: [tg_jaccard_nbor_ap_batch].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Similarity/jaccard/single_source/tg_jaccard_nbor_ss.gsql
Successfully created queries: [tg_jaccard_nbor_ss].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Similarity/cosine/all_pairs/tg_cosine_nbor_ap_batch.gsql
Warning in query tg_cosine_nbor_ap_batch (WARN-5): line 80, col 39
The comparison 'divisor==0' may lead to unexpected behavior because it involves
equality test between float/double numeric values. We suggest to do such
comparison with an error margin, e.g. 'abs((divisor) - (0)) < epsilon', where
epsilon is a very small positive value of your choice, such as 0.0001.
Successfully created queries: [tg_cosine_nbor_ap_batch].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Similarity/cosine/single_source/tg_cosine_nbor_ss.gsql
Successfully created queries: [tg_cosine_nbor_ss].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Topological Link Prediction/preferential_attachment/tg_preferential_attachment.gsql
Successfully created queries: [tg_preferential_attachment].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Topological Link Prediction/resource_allocation/tg_resource_allocation.gsql
Successfully created queries: [tg_resource_allocation].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Topological Link Prediction/same_community/tg_same_community.gsql
Successfully created queries: [tg_same_community].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Topological Link Prediction/adamic_adar/tg_adamic_adar.gsql
Successfully created queries: [tg_adamic_adar].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Topological Link Prediction/total_neighbors/tg_total_neighbors.gsql
Successfully created queries: [tg_total_neighbors].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Topological Link Prediction/common_neighbors/tg_common_neighbors.gsql
Successfully created queries: [tg_common_neighbors].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/greedy_graph_coloring/tg_greedy_graph_coloring.gsql
Successfully created queries: [tg_greedy_graph_coloring].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/maximal_independent_set/deterministic/tg_maximal_indep_set.gsql
Successfully created queries: [tg_maximal_indep_set].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/maximal_independent_set/random/tg_maximal_indep_set_random.gsql
Successfully created queries: [tg_maximal_indep_set_random].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/k_nearest_neighbors/all_pairs/tg_knn_cosine_all.gsql

Semantic Check Error in query tg_knn_cosine_all (SEM-45): line 56, col 49
The tuple name or the function tg_knn_cosine_all_sub is not defined.
Saved as draft query with type/semantic error: [tg_knn_cosine_all].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/k_nearest_neighbors/all_pairs/tg_knn_cosine_all_sub.gsql
Successfully created queries: [tg_knn_cosine_all_sub].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/k_nearest_neighbors/single_source/tg_knn_cosine_ss.gsql
Successfully created queries: [tg_knn_cosine_ss].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/k_nearest_neighbors/cross_validation/tg_knn_cosine_cv_sub.gsql
Successfully created queries: [tg_knn_cosine_cv_sub].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Classification/k_nearest_neighbors/cross_validation/tg_knn_cosine_cv.gsql
Successfully created queries: [tg_knn_cosine_cv].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/GraphML/Embeddings/EmbeddingSimilarity/pairwise/tg_embedding_pairwise_cosine_sim.gsql
Successfully created queries: [tg_embedding_pairwise_cosine_similarity].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/GraphML/Embeddings/EmbeddingSimilarity/single_source/tg_embedding_cosine_sim.gsql
Successfully created queries: [tg_embedding_cosine_similarity].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/GraphML/Embeddings/weisfeiler_lehman/tg_weisfeiler_lehman.gsql
Successfully created queries: [tg_weisfeiler_lehman].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/GraphML/Embeddings/FastRP/tg_fastRP.gsql
Warning in query tg_fastRP (WARN-5): line 209, col 12
The comparison 'mr<=p1' may lead to unexpected behavior because it involves
equality test between float/double numeric values. We suggest to do such
comparison with an error margin, e.g. 'mr<=p1 + epsilon', where epsilon is a
very small positive value of your choice, such as 0.0001.
Warning in query tg_fastRP (WARN-5): line 211, col 17
The comparison 'mr<=p1+p2' may lead to unexpected behavior because it involves
equality test between float/double numeric values. We suggest to do such
comparison with an error margin, e.g. 'mr<=p1+p2 + epsilon', where epsilon is a
very small positive value of your choice, such as 0.0001.
Warning in query tg_fastRP (WARN-5): line 238, col 13
The comparison 'square_sum==0.0' may lead to unexpected behavior because it
involves equality test between float/double numeric values. We suggest to do
such comparison with an error margin, e.g. 'abs((square_sum) - (0.0)) <
epsilon', where epsilon is a very small positive value of your choice, such as
0.0001.
Successfully created queries: [tg_fastRP].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/speaker-listener_label_propagation/tg_slpa.gsql
Successfully created queries: [tg_slpa].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/label_propagation/tg_label_prop.gsql
Successfully created queries: [tg_label_prop].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/k_means/tg_kmeans_sub.gsql

Type Check Error in query tg_kmeans_sub (TYP-158): line 43, col 33
't.embeddings' indicates no valid vertex type.
Possible reasons:

- The expression refers to a primary_id, which is not directly
usable in the query body. To use primary_id, declare it as an
attribute. E.g "CREATE VERTEX Person (PRIMARY_ID ssn string, ssn string, age
int)"
- The expression has misspelled an attribute, or a vertex name

Saved as draft query with type/semantic error: [tg_kmeans_sub].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/k_means/tg_kmeans.gsql

Type Check Error in query tg_kmeans (TYP-5401): line 50, col 29
Query 'tg_kmeans_sub' cannot be used as an expression, because it does not have
a return type.
Saved as draft query with type/semantic error: [tg_kmeans].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/triangle_counting/fast/tg_tri_count_fast.gsql
Successfully created queries: [tg_tri_count_fast].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/triangle_counting/standard/tg_tri_count.gsql
Successfully created queries: [tg_tri_count].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/connected_components/strongly_connected_components/small_world/tg_scc_small_world.gsql
Successfully created queries: [tg_scc_small_world].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/connected_components/strongly_connected_components/standard/tg_scc.gsql
Successfully created queries: [tg_scc].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/connected_components/weakly_connected_components/small_world/tg_wcc_small_world.gsql
Successfully created queries: [tg_wcc_small_world].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/connected_components/weakly_connected_components/standard/tg_wcc.gsql
Successfully created queries: [tg_wcc].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/k_core/tg_kcore.gsql
Successfully created queries: [tg_kcore].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/map_equation/tg_map_equation.gsql
Successfully created queries: [tg_map_equation].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/local_clustering_coefficient/tg_lcc.gsql
Successfully created queries: [tg_lcc].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/louvain/tg_louvain.gsql
Warning in query tg_louvain (WARN-5): line 97, col 25
The comparison '-t.@max_best_move.weight==t.@sum_cc_weight' may lead to
unexpected behavior because it involves equality test between float/double
numeric values. We suggest to do such comparison with an error margin, e.g.
'abs((-t.@max_best_move.weight) - (t.@sum_cc_weight)) < epsilon', where epsilon
is a very small positive value of your choice, such as 0.0001.
Warning in query tg_louvain (WARN-5): line 173, col 29
The comparison '-s.@max_best_move.weight==s.@sum_cc_weight' may lead to
unexpected behavior because it involves equality test between float/double
numeric values. We suggest to do such comparison with an error margin, e.g.
'abs((-s.@max_best_move.weight) - (s.@sum_cc_weight)) < epsilon', where epsilon
is a very small positive value of your choice, such as 0.0001.
Successfully created queries: [tg_louvain].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/cycle_component/tg_cycle_component.gsql
Successfully created queries: [tg_cycle_component].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/shortest_path/unweighted/tg_shortest_ss_no_wt.gsql
Successfully created queries: [tg_shortest_ss_no_wt].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/shortest_path/weighted/any_sign/tg_shortest_ss_any_wt.gsql
Successfully created queries: [tg_shortest_ss_any_wt].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/shortest_path/weighted/positive/summary/tg_shortest_ss_pos_wt.gsql
Warning in query tg_shortest_ss_pos_wt (WARN-5): line 102, col 20
The comparison 's.@min_prev_path!=-1' may lead to unexpected behavior because it
involves equality test between float/double numeric values. We suggest to do
such comparison with an error margin, e.g. 'abs((s.@min_prev_path) - (-1)) >
epsilon', where epsilon is a very small positive value of your choice, such as
0.0001.
Successfully created queries: [tg_shortest_ss_pos_wt].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/shortest_path/weighted/positive/traceback/tg_shortest_ss_pos_wt_tb.gsql
Warning in query tg_shortest_ss_pos_wt_tb (WARN-5): line 123, col 20
The comparison 's.@min_prev_min_path!=-1' may lead to unexpected behavior
because it involves equality test between float/double numeric values. We
suggest to do such comparison with an error margin, e.g.
'abs((s.@min_prev_min_path) - (-1)) > epsilon', where epsilon is a very small
positive value of your choice, such as 0.0001.
Successfully created queries: [tg_shortest_ss_pos_wt_tb].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/cycle_detection/count/tg_cycle_detection_count.gsql
Successfully created queries: [tg_cycle_detection_count].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/cycle_detection/full_result/standard/tg_cycle_detection.gsql
Successfully created queries: [tg_cycle_detection].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/cycle_detection/full_result/batch/tg_cycle_detection_batch.gsql
Warning in query tg_cycle_detection_batch (WARN-2): line 61, col 37
unsatisfiable pattern e_type_set
Warning in query tg_cycle_detection_batch (WARN-2): line 61, col 37
unsatisfiable pattern e_type_set
Warning in query tg_cycle_detection_batch (WARN-2): line 61, col 35
unsatisfiable pattern -(e_type_set:e)- :t
Warning in query tg_cycle_detection_batch (WARN-2): line 61, col 35
unsatisfiable pattern -(e_type_set:e)- :t
Warning in query tg_cycle_detection_batch (WARN-2): line 61, col 26
unsatisfiable pattern Active:s -(e_type_set:e)- :t

Type Check Error in query tg_cycle_detection_batch (TYP-8029): line 61, col 21
the pattern "Active:s -(e_type_set:e)- :t" has an undirected edge, but the graph
does not contain any undirected edges

Saved as draft query with type/semantic error: [tg_cycle_detection_batch].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/estimated_diameter/approximate/tg_estimate_diameter.gsql

Semantic Check Error in query tg_estimate_diameter (SEM-45): line 52, col 34
The tuple name or the function tg_max_BFS_depth is not defined.
Saved as draft query with type/semantic error: [tg_estimate_diameter].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/estimated_diameter/max_bfs/tg_max_BFS_depth.gsql
Successfully created queries: [tg_max_BFS_depth].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/astar_shortest_path/tg_astar.gsql
Successfully created queries: [tg_astar].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/path_between_two_vertices/one_direction/tg_all_path.gsql
Successfully created queries: [tg_all_path].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/path_between_two_vertices/bidirection/tg_all_path_bidirection.gsql
Successfully created queries: [tg_all_path_bidirection].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/minimum_spanning_forest/tg_msf.gsql
Successfully created queries: [tg_msf].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/minimum_spanning_tree/tg_mst.gsql
Successfully created queries: [tg_mst].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/bfs/tg_bfs.gsql
Successfully created queries: [tg_bfs].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Path/maxflow/tg_maxflow.gsql
Warning in query tg_maxflow (WARN-5): line 129, col 25
The comparison 'fl-@@group_by_flow_accum.get(s,t).flow>=@@max_cap_threshold' may
lead to unexpected behavior because it involves equality test between
float/double numeric values. We suggest to do such comparison with an error
margin, e.g. 'fl-@@group_by_flow_accum.get(s,t).flow>=@@max_cap_threshold -
epsilon', where epsilon is a very small positive value of your choice, such as
0.0001.
Warning in query tg_maxflow (WARN-5): line 140, col 25
The comparison '@@group_by_flow_accum.get(t,s).flow>=@@max_cap_threshold' may
lead to unexpected behavior because it involves equality test between
float/double numeric values. We suggest to do such comparison with an error
margin, e.g. '@@group_by_flow_accum.get(t,s).flow>=@@max_cap_threshold -
epsilon', where epsilon is a very small positive value of your choice, such as
0.0001.
Warning in query tg_maxflow (WARN-5): line 211, col 20
The comparison '@@group_by_flow_accum.get(s,t).flow>=min_flow_threshhold' may
lead to unexpected behavior because it involves equality test between
float/double numeric values. We suggest to do such comparison with an error
margin, e.g. '@@group_by_flow_accum.get(s,t).flow>=min_flow_threshhold -
epsilon', where epsilon is a very small positive value of your choice, such as
0.0001.
Successfully created queries: [tg_maxflow].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/betweenness/tg_betweenness_cent.gsql
Successfully created queries: [tg_betweenness_cent].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/closeness/approximate/tg_closeness_cent_approx.gsql
Successfully created queries: [tg_closeness_cent_approx].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/closeness/exact/tg_closeness_cent.gsql
Successfully created queries: [tg_closeness_cent].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/eigenvector/tg_eigenvector_cent.gsql
Warning in query tg_eigenvector_cent (WARN-5): line 85, col 19
The comparison 's.@sum_eigen_value==1.0' may lead to unexpected behavior because
it involves equality test between float/double numeric values. We suggest to do
such comparison with an error margin, e.g. 'abs((s.@sum_eigen_value) - (1.0)) <
epsilon', where epsilon is a very small positive value of your choice, such as
0.0001.
Successfully created queries: [tg_eigenvector_cent].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/influence_maximization/greedy/tg_influence_maximization_greedy.gsql
Successfully created queries: [tg_influence_maximization_greedy].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/influence_maximization/CELF/tg_influence_maximization_CELF.gsql
Warning in query tg_influence_maximization_CELF (WARN-5): line 83, col 19
The comparison 's.@influence_value>=score' may lead to unexpected behavior
because it involves equality test between float/double numeric values. We
suggest to do such comparison with an error margin, e.g.
's.@influence_value>=score - epsilon', where epsilon is a very small positive
value of your choice, such as 0.0001.
Successfully created queries: [tg_influence_maximization_CELF].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/degree/unweighted/tg_degree_cent.gsql
Successfully created queries: [tg_degree_cent].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/degree/weighted/tg_weighted_degree_cent.gsql
Successfully created queries: [tg_weighted_degree_cent].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/pagerank/global/unweighted/tg_pagerank.gsql
Successfully created queries: [tg_pagerank].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/pagerank/global/weighted/tg_pagerank_wt.gsql
Successfully created queries: [tg_pagerank_wt].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/pagerank/personalized/multi_source/tg_pagerank_pers.gsql
Successfully created queries: [tg_pagerank_pers].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/pagerank/personalized/all_pairs/tg_pagerank_pers_ap_batch.gsql
Successfully created queries: [tg_pagerank_pers_ap_batch].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/harmonic/tg_harmonic_cent.gsql
Successfully created queries: [tg_harmonic_cent].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/article_rank/tg_article_rank.gsql
Successfully created queries: [tg_article_rank].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Patterns/frequent_pattern_mining/tg_fpm_pre.gsql

Type Check Error in query tg_fpm_pre (TYP-158): line 47, col 12
's.item_list' indicates no valid vertex type.
Possible reasons:

- The expression refers to a primary_id, which is not directly
usable in the query body. To use primary_id, declare it as an
attribute. E.g "CREATE VERTEX Person (PRIMARY_ID ssn string, ssn string, age
int)"
- The expression has misspelled an attribute, or a vertex name

Saved as draft query with type/semantic error: [tg_fpm_pre].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Patterns/frequent_pattern_mining/tg_fpm.gsql
Warning in query tg_fpm (WARN-7): line 151, col 9
POST-ACCUM clauses binding to multiple aliases ([s, t]) will be deprecated soon.
Please separate into 2 POST-ACCUM clauses, one for each alias.
Warning in query tg_fpm (WARN-7): line 151, col 9
POST-ACCUM clauses binding to multiple aliases ([s, t]) will be deprecated soon.
Please separate into 2 POST-ACCUM clauses, one for each alias.

Type Check Error in query tg_fpm (TYP-158): line 80, col 33
's.item_list' indicates no valid vertex type.
Possible reasons:

- The expression refers to a primary_id, which is not directly
usable in the query body. To use primary_id, declare it as an
attribute. E.g "CREATE VERTEX Person (PRIMARY_ID ssn string, ssn string, age
int)"
- The expression has misspelled an attribute, or a vertex name

Saved as draft query with type/semantic error: [tg_fpm].
Installing queries for graph: MyGraph
Start installing queries, about 1 minute ...
tg_tri_count_fast query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_tri_count_fast?v_type=VALUE&e_type=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_tri_count query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_tri_count?v_type=VALUE&e_type=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_all_path query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_all_path?v_source=VALUE&v_source.type=VERTEX_TYPE&target_v=VALUE&target_v.type=VERTEX_TYPE&[depth=VALUE]&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_embedding_pairwise_cosine_similarity query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_embedding_pairwise_cosine_similarity?v1=VALUE&v1.type=VERTEX_TYPE&v2=VALUE&v2.type=VERTEX_TYPE&embedding_dimension=VALUE&embedding_attribute=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_common_neighbors query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_common_neighbors?v_source=VALUE&v_source.type=VERTEX_TYPE&v_target=VALUE&v_target.type=VERTEX_TYPE&e_type_set=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_wcc query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_wcc?v_type_set=VALUE&e_type_set=VALUE&[print_limit=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_shortest_ss_no_wt query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_shortest_ss_no_wt?source=VALUE&source.type=VERTEX_TYPE&v_type_set=VALUE&e_type_set=VALUE&[print_limit=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_maximal_indep_set query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_maximal_indep_set?v_type=VALUE&e_type=VALUE&[maximum_iteration=VALUE]&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_scc_small_world query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_scc_small_world?v_type=VALUE&e_type=VALUE&reverse_e_type=VALUE&[threshold=VALUE]&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_all_path_bidirection query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_all_path_bidirection?v_source=VALUE&v_source.type=VERTEX_TYPE&target_v=VALUE&target_v.type=VERTEX_TYPE&e_type_set=VALUE&reverse_e_type_set=VALUE&[depth=VALUE]&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_pagerank_pers_ap_batch query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_pagerank_pers_ap_batch?v_type=VALUE&e_type=VALUE&[max_change=VALUE]&[maximum_iteration=VALUE]&[damping=VALUE]&[top_k=VALUE]&batch_num=VALUE&print_results=VALUE&file_path=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_embedding_cosine_similarity query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_embedding_cosine_similarity?v1=VALUE&v1.type=VERTEX_TYPE&vert_types=VALUE&embedding_dimension=VALUE&k=VALUE&embedding_attribute=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_eigenvector_cent query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_eigenvector_cent?v_type_set=VALUE&e_type_set=VALUE&[maximum_iteration=VALUE]&[conv_limit=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_pagerank_pers query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_pagerank_pers?source[INDEX]=VALUE&source[INDEX].type=VERTEX_TYPE&e_type=VALUE&[max_change=VALUE]&[maximum_iteration=VALUE]&[damping=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_mst query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_mst?opt_source=VALUE&opt_source.type=VERTEX_TYPE&v_type_set=VALUE&e_type_set=VALUE&weight_attribute=VALUE&weight_type=VALUE&[maximum_iteration=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_bfs query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_bfs?v_type_set=VALUE&e_type_set=VALUE&[max_hops=VALUE]&v_start=VALUE&v_start.type=VERTEX_TYPE&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_pagerank_wt query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_pagerank_wt?v_type=VALUE&e_type=VALUE&weight_attribute=VALUE&[max_change=VALUE]&[maximum_iteration=VALUE]&[damping=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_degree_cent query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_degree_cent?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&[in_degree=VALUE]&[out_degree=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_shortest_ss_any_wt query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_shortest_ss_any_wt?source=VALUE&source.type=VERTEX_TYPE&v_type_set=VALUE&e_type_set=VALUE&weight_attribute=VALUE&weight_type=VALUE&[print_limit=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_resource_allocation query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_resource_allocation?v_source=VALUE&v_source.type=VERTEX_TYPE&v_target=VALUE&v_target.type=VERTEX_TYPE&e_type_set=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_greedy_graph_coloring query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_greedy_graph_coloring?v_type_set=VALUE&e_type_set=VALUE&[max_colors=VALUE]&[print_color_count=VALUE]&[print_stats=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_wcc_small_world query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_wcc_small_world?v_type=VALUE&e_type=VALUE&[threshold=VALUE]&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_scc query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_scc?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&top_k_dist=VALUE&print_limit=VALUE&[maximum_iteration=VALUE]&[iter_wcc=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_maximal_indep_set_random query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_maximal_indep_set_random?v_type_set=VALUE&e_type_set=VALUE&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_max_BFS_depth query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_max_BFS_depth?source=VALUE&source.type=VERTEX_TYPE&e_type_set=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_harmonic_cent query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_harmonic_cent?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&[max_hops=VALUE]&[top_k=VALUE]&[wf=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_adamic_adar query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_adamic_adar?v_source=VALUE&v_source.type=VERTEX_TYPE&v_target=VALUE&v_target.type=VERTEX_TYPE&e_type_set=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_louvain query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_louvain?v_type_set=VALUE&e_type_set=VALUE&[weight_attribute=VALUE]&[maximum_iteration=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[print_stats=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_influence_maximization_greedy query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_influence_maximization_greedy?v_type=VALUE&e_type=VALUE&weight_attribute=VALUE&top_k=VALUE&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_jaccard_nbor_ap_batch query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_jaccard_nbor_ap_batch?[top_k=VALUE]&v_type_set=VALUE&feat_v_type=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&similarity_edge=VALUE&[src_batch_num=VALUE]&[nbor_batch_num=VALUE]&[print_results=VALUE]&[print_limit=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_total_neighbors query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_total_neighbors?v_source=VALUE&v_source.type=VERTEX_TYPE&v_target=VALUE&v_target.type=VERTEX_TYPE&e_type_set=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_lcc query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_lcc?v_type=VALUE&e_type=VALUE&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_knn_cosine_cv_sub query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_knn_cosine_cv_sub?source=VALUE&source.type=VERTEX_TYPE&e_type_set=VALUE&reverse_e_type_set=VALUE&v_label=VALUE&weight_attribute=VALUE&max_k=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_betweenness_cent query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_betweenness_cent?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type=VALUE&[max_hops=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_cosine_nbor_ss query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_cosine_nbor_ss?source=VALUE&source.type=VERTEX_TYPE&e_type_set=VALUE&reverse_e_type_set=VALUE&weight_attribute=VALUE&top_k=VALUE&print_limit=VALUE&[print_results=VALUE]&[file_path=VALUE]&[similarity_edge=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_closeness_cent query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_closeness_cent?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type=VALUE&[max_hops=VALUE]&[top_k=VALUE]&[wf=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_knn_cosine_all_sub query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_knn_cosine_all_sub?source=VALUE&source.type=VERTEX_TYPE&e_type_set=VALUE&reverse_e_type_set=VALUE&weight_attribute=VALUE&label=VALUE&top_k=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_slpa query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_slpa?v_type_set=VALUE&e_type_set=VALUE&threshold=VALUE&maximum_iteration=VALUE&print_limit=VALUE&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_pagerank query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_pagerank?v_type=VALUE&e_type=VALUE&[max_change=VALUE]&[maximum_iteration=VALUE]&[damping=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_cycle_detection query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_cycle_detection?v_type_set=VALUE&e_type_set=VALUE&depth=VALUE&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_cosine_nbor_ap_batch query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_cosine_nbor_ap_batch?v_type=VALUE&e_type=VALUE&edge_attribute=VALUE&top_k=VALUE&[print_results=VALUE]&file_path=VALUE&similarity_edge=VALUE&[num_of_batches=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_astar query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_astar?source_vertex=VALUE&source_vertex.type=VERTEX_TYPE&target_vertex=VALUE&target_vertex.type=VERTEX_TYPE&e_type_set=VALUE&weight_type=VALUE&latitude=VALUE&longitude=VALUE&weight_attribute=VALUE&[print_stats=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_same_community query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_same_community?v_source=VALUE&v_source.type=VERTEX_TYPE&v_target=VALUE&v_target.type=VERTEX_TYPE&community_attribute=VALUE&community_attr_type=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_weisfeiler_lehman query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_weisfeiler_lehman?v_type=VALUE&e_type=VALUE&DEPTH=VALUE&print_limit=VALUE&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_cycle_component query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_cycle_component?v_type=VALUE&e_type=VALUE&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_map_equation query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_map_equation?v_type=VALUE&e_type=VALUE&result_attribute=VALUE&[weight_attribute=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_knn_cosine_cv query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_knn_cosine_cv?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&weight_attribute=VALUE&label=VALUE&min_k=VALUE&max_k=VALUE'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_jaccard_nbor_ss query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_jaccard_nbor_ss?source=VALUE&source.type=VERTEX_TYPE&e_type=VALUE&reverse_e_type=VALUE&[top_k=VALUE]&[print_results=VALUE]&[similarity_edge_type=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_article_rank query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_article_rank?v_type=VALUE&e_type=VALUE&[max_change=VALUE]&[maximum_iteration=VALUE]&[damping=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_weighted_degree_cent query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_weighted_degree_cent?v_type=VALUE&e_type=VALUE&reverse_e_type=VALUE&weight_attribute=VALUE&[in_degree=VALUE]&[out_degree=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_preferential_attachment query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_preferential_attachment?v_source=VALUE&v_source.type=VERTEX_TYPE&v_target=VALUE&v_target.type=VERTEX_TYPE&e_type_set=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_label_prop query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_label_prop?v_type_set=VALUE&e_type_set=VALUE&maximum_iteration=VALUE&print_limit=VALUE&[print_results=VALUE]&[file_path=VALUE]&[result_attribute=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_shortest_ss_pos_wt query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_shortest_ss_pos_wt?source=VALUE&source.type=VERTEX_TYPE&v_type_set=VALUE&e_type_set=VALUE&weight_attribute=VALUE&weight_type=VALUE&[epsilon=VALUE]&[print_results=VALUE]&[print_limit=VALUE]&[display_edges=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_kcore query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_kcore?v_type=VALUE&e_type=VALUE&[k_min=VALUE]&[k_max=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[print_all_k=VALUE]&[show_shells=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_cycle_detection_count query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_cycle_detection_count?v_type_set=VALUE&e_type_set=VALUE&depth=VALUE&batches=VALUE&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_closeness_cent_approx query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_closeness_cent_approx?v_type_set=VALUE&e_type_set=VALUE&reverse_e_type=VALUE&[top_k=VALUE]&[k=VALUE]&[max_hops=VALUE]&[epsilon=VALUE]&[print_results=VALUE]&[file_path=VALUE]&[debug=VALUE]&[sample_index=VALUE]&[max_size=VALUE]&[wf=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_knn_cosine_ss query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_knn_cosine_ss?source=VALUE&source.type=VERTEX_TYPE&v_type_set=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&weight_attribute=VALUE&label=VALUE&top_k=VALUE&[print_results=VALUE]&[file_path=VALUE]&[result_attribute=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_fastRP query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_fastRP?v_type_set=VALUE&e_type_set=VALUE&output_v_type_set=VALUE&iteration_weights=VALUE&beta=VALUE&embedding_dimension=VALUE&[default_index=VALUE]&default_length=VALUE&[default_weight=VALUE]&embedding_dim_map=VALUE&[sampling_constant=VALUE]&[random_seed=VALUE]&[result_attribute=VALUE]&[component_attribute=VALUE]&[batch_number=VALUE]&[filepath=VALUE]&[print_results=VALUE]&[choose_k=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_influence_maximization_CELF query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_influence_maximization_CELF?v_type=VALUE&e_type=VALUE&weight_attribute=VALUE&top_k=VALUE&[print_results=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_shortest_ss_pos_wt_tb query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_shortest_ss_pos_wt_tb?source=VALUE&source.type=VERTEX_TYPE&v_type_set=VALUE&e_type_set=VALUE&weight_attribute=VALUE&weight_type=VALUE&[epsilon=VALUE]&[print_results=VALUE]&[print_limit=VALUE]&[display_edges=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[write_size=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_maxflow query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_maxflow?source=VALUE&source.type=VERTEX_TYPE&sink=VALUE&sink.type=VERTEX_TYPE&v_type=VALUE&e_type_set=VALUE&reverse_e_type_set=VALUE&cap_attr=VALUE&cap_type=VALUE&[min_flow_threshhold=VALUE]&[print_results=VALUE]&[display_edges=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_msf query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_msf?v_type_set=VALUE&e_type_set=VALUE&weight_attribute=VALUE&weight_type=VALUE&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
Select 'm1' as compile server, now connecting ...
Node 'm1' is prepared as compile server.

[======================================================================================================] 100% (62/62)
Query installation finished.
======================================== MyGraph2 ========================================
Dropping the graph MyGraph2...
Successfully dropped jobs on the graph 'MyGraph2': [loading_job].
All jobs on the graph 'MyGraph2' are dropped.
All queries are dropped.
The graph MyGraph2 is dropped.
Finished dropping graph MyGraph2.
--------------------------------------------------------------------------------
Running: Creating schema /home/tigergraph/gsql-graph-algorithms/algorithms_test/gsql/MyGraph2/1_create_schema.gsql
The graph MyGraph2 is created.
Successfully created schema change jobs: [change_schema_of_MyGraph].
WARNING: When modifying the graph schema, reinstalling all affected queries is required, and the duration of this process may vary based on the number and complexity of the queries. To skip query reinstallation, you can run with the '-N' option, but manual reinstallation of queries will be necessary afterwards.
Kick off schema change job change_schema_of_MyGraph
Doing schema change on graph 'MyGraph2' (current version: 0)
Trying to add local vertex 'MyNode' to the graph 'MyGraph2'.
Trying to add local edge 'MyEdge' and its reverse edge 'rev_MyEdge' to the graph 'MyGraph2'.

Graph MyGraph2 updated to new version 1
The job change_schema_of_MyGraph completes in 0.933 seconds!
Local schema change succeeded.
Successfully dropped jobs on the graph 'MyGraph2': [change_schema_of_MyGraph].
--------------------------------------------------------------------------------
Running: Creating loading job /home/tigergraph/gsql-graph-algorithms/algorithms_test/gsql/MyGraph2/2_create_loading_job.gsql
Using graph 'MyGraph2'
Successfully created loading jobs: [loading_job].
--------------------------------------------------------------------------------
Running loading job for /home/tigergraph/mydata/northeast_usa/out.dimacs9-NE...
[Tip: Use "CTRL + C" to stop displaying the loading status update, then use "SHOW LOADING STATUS <jobid>" to track the loading progress again]
[Tip: Manage loading jobs with "ABORT/RESUME LOADING JOB <jobid>"]
Running the following loading job:
  Job name: loading_job
  Jobid: MyGraph2.loading_job.file.m1.1720513297218
  Log directory: /home/tigergraph/tigergraph/log/fileLoader/MyGraph2.loading_job.file.m1.1720513297218
Job "MyGraph2.loading_job.file.m1.1720513297218" loading status
Current timestamp is 2024-07-09 08:21:42.475
Loading status was last updated at 2024-07-09 08:21:42.261.
[FINISHED] m1 ( Finished: 1 / Total: 1 )
  +-------------------------------------------------------------------------------------------------------+
  |                    FILENAME |   LINES |   OBJECTS |   ERRORS |   AVG SPEED |   DURATION |   PERCENTAGE|
  |northeast_usa/out.dimacs9-NE | 3868020 |  11604060 |        0 |    804 kl/s |     4.81 s |        100 %|
  +-------------------------------------------------------------------------------------------------------+
LOAD SUCCESSFUL for loading jobid: MyGraph2.loading_job.file.m1.1720513297218
  Job ID: MyGraph2.loading_job.file.m1.1720513297218------------------------------------------------------+
  Elapsed time: 5 sec
  Log directory: /home/tigergraph/tigergraph/log/fileLoader/MyGraph2.loading_job.file.m1.1720513297218
  Summary: /home/tigergraph/tigergraph/log/fileLoader/MyGraph2.loading_job.file.m1.1720513297218/summary

Finished running loading job for /home/tigergraph/mydata/northeast_usa/out.dimacs9-NE.
--------------------------------------------------------------------------------
No queries to install for graph: MyGraph2
algorithms_test (ALGOS-263) $
algorithms_test (ALGOS-263) $ ll
total 40
-rwxr-xr-x 1 tigergraph tigergraph 2369 Jul  5 09:40 1_dataset.sh
-rwxr-xr-x 1 tigergraph tigergraph 6042 Jul  8 06:24 2_setup.sh
-rwxr-xr-x 1 tigergraph tigergraph 5213 Jul  8 09:08 3_run.sh
drwxrwxr-x 2 tigergraph tigergraph 4096 Jul  4 08:34 baseline
drwxr-xr-x 2 tigergraph tigergraph 4096 Jul  9 08:16 config
drwxrwxr-x 4 tigergraph tigergraph 4096 Jul  8 02:24 gsql
drwxr-xr-x 2 tigergraph tigergraph 4096 Jul  8 03:34 mem
-rw-rw-r-- 1 tigergraph tigergraph    0 Jul  4 08:38 ReadMe.md
drwxr-xr-x 2 tigergraph tigergraph 4096 Jul  8 06:53 tools
algorithms_test (ALGOS-263) $
```

# Run
```
algorithms_test (ALGOS-263) $ ./3_run.sh
==================== topological_link_prediction/tg_preferential_attachment run 0 ====================
Starting curl command for query: tg_preferential_attachment on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_preferential_attachment/result.json
Duration has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_preferential_attachment/duration.txt
Finished curl command for query: tg_preferential_attachment on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_preferential_attachment/memory.txt
==================== topological_link_prediction/tg_resource_allocation run 0 ====================
Starting curl command for query: tg_resource_allocation on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_resource_allocation/result.json
Duration has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_resource_allocation/duration.txt
Finished curl command for query: tg_resource_allocation on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_resource_allocation/memory.txt
==================== topological_link_prediction/tg_same_community run 0 ====================
Starting curl command for query: tg_same_community on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_same_community/result.json
Duration has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_same_community/duration.txt
Finished curl command for query: tg_same_community on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_same_community/memory.txt
==================== topological_link_prediction/tg_adamic_adar run 0 ====================
Starting curl command for query: tg_adamic_adar on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_adamic_adar/result.json
Duration has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_adamic_adar/duration.txt
Finished curl command for query: tg_adamic_adar on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_adamic_adar/memory.txt
==================== topological_link_prediction/tg_total_neighbors run 0 ====================
Starting curl command for query: tg_total_neighbors on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_total_neighbors/result.json
Duration has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_total_neighbors/duration.txt
Finished curl command for query: tg_total_neighbors on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/topological_link_prediction/tg_total_neighbors/memory.txt
==================== classification/tg_greedy_graph_coloring run 0 ====================
Starting curl command for query: tg_greedy_graph_coloring on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16777220.RESTPP_1_1.1720513538258.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/classification/tg_greedy_graph_coloring/result.json
Duration has been written to /home/tigergraph/data/algos/classification/tg_greedy_graph_coloring/duration.txt
Finished curl command for query: tg_greedy_graph_coloring on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/classification/tg_greedy_graph_coloring/memory.txt
==================== classification/tg_maximal_indep_set run 0 ====================
Starting curl command for query: tg_maximal_indep_set on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/classification/tg_maximal_indep_set/result.json
Duration has been written to /home/tigergraph/data/algos/classification/tg_maximal_indep_set/duration.txt
Finished curl command for query: tg_maximal_indep_set on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/classification/tg_maximal_indep_set/memory.txt
==================== classification/tg_knn_cosine_ss run 0 ====================
Starting curl command for query: tg_knn_cosine_ss on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/classification/tg_knn_cosine_ss/result.json
Duration has been written to /home/tigergraph/data/algos/classification/tg_knn_cosine_ss/duration.txt
Finished curl command for query: tg_knn_cosine_ss on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/classification/tg_knn_cosine_ss/memory.txt
==================== classification/tg_knn_cosine_cv run 0 ====================
Starting curl command for query: tg_knn_cosine_cv on graph: MyGraph
Error: Runtime Error: divider is zero.
Result has been written to /home/tigergraph/data/algos/classification/tg_knn_cosine_cv/result.json
Duration has been written to /home/tigergraph/data/algos/classification/tg_knn_cosine_cv/duration.txt
Finished curl command for query: tg_knn_cosine_cv on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/classification/tg_knn_cosine_cv/memory.txt
==================== community/tg_slpa run 0 ====================
Starting curl command for query: tg_slpa on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16777225.RESTPP_1_1.1720514490906.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/community/tg_slpa/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_slpa/duration.txt
Finished curl command for query: tg_slpa on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_slpa/memory.txt
==================== community/tg_label_prop run 0 ====================
Starting curl command for query: tg_label_prop on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_label_prop/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_label_prop/duration.txt
Finished curl command for query: tg_label_prop on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_label_prop/memory.txt
==================== community/tg_tri_count_fast run 0 ====================
Starting curl command for query: tg_tri_count_fast on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_tri_count_fast/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_tri_count_fast/duration.txt
Finished curl command for query: tg_tri_count_fast on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_tri_count_fast/memory.txt
==================== community/tg_tri_count run 0 ====================
Starting curl command for query: tg_tri_count on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_tri_count/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_tri_count/duration.txt
Finished curl command for query: tg_tri_count on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_tri_count/memory.txt
==================== community/tg_scc run 0 ====================
Starting curl command for query: tg_scc on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_scc/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_scc/duration.txt
Finished curl command for query: tg_scc on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_scc/memory.txt
==================== community/tg_scc_small_world run 0 ====================
Starting curl command for query: tg_scc_small_world on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_scc_small_world/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_scc_small_world/duration.txt
Finished curl command for query: tg_scc_small_world on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_scc_small_world/memory.txt
==================== community/tg_wcc run 0 ====================
Starting curl command for query: tg_wcc on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_wcc/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_wcc/duration.txt
Finished curl command for query: tg_wcc on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_wcc/memory.txt
==================== community/tg_wcc_small_world run 0 ====================
Starting curl command for query: tg_wcc_small_world on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_wcc_small_world/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_wcc_small_world/duration.txt
Finished curl command for query: tg_wcc_small_world on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_wcc_small_world/memory.txt
==================== community/tg_kcore run 0 ====================
Starting curl command for query: tg_kcore on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_kcore/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_kcore/duration.txt
Finished curl command for query: tg_kcore on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_kcore/memory.txt
==================== community/tg_map_equation run 0 ====================
Starting curl command for query: tg_map_equation on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_map_equation/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_map_equation/duration.txt
Finished curl command for query: tg_map_equation on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_map_equation/memory.txt
==================== community/tg_lcc run 0 ====================
Starting curl command for query: tg_lcc on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_lcc/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_lcc/duration.txt
Finished curl command for query: tg_lcc on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_lcc/memory.txt
==================== community/tg_louvain run 0 ====================
Starting curl command for query: tg_louvain on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_louvain/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_louvain/duration.txt
Finished curl command for query: tg_louvain on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_louvain/memory.txt
==================== path/tg_cycle_component run 0 ====================
Starting curl command for query: tg_cycle_component on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/path/tg_cycle_component/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_cycle_component/duration.txt
Finished curl command for query: tg_cycle_component on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_cycle_component/memory.txt
==================== path/tg_shortest_ss_no_wt run 0 ====================
Starting curl command for query: tg_shortest_ss_no_wt on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_no_wt/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_no_wt/duration.txt
Finished curl command for query: tg_shortest_ss_no_wt on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_no_wt/memory.txt
==================== path/tg_shortest_ss_any_wt run 0 ====================
Starting curl command for query: tg_shortest_ss_any_wt on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16777235.RESTPP_1_1.1720516010379.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_any_wt/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_any_wt/duration.txt
Finished curl command for query: tg_shortest_ss_any_wt on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_any_wt/memory.txt
==================== path/tg_shortest_ss_pos_wt run 0 ====================
Starting curl command for query: tg_shortest_ss_pos_wt on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_pos_wt/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_pos_wt/duration.txt
Finished curl command for query: tg_shortest_ss_pos_wt on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_pos_wt/memory.txt
==================== path/tg_shortest_ss_pos_wt_tb run 0 ====================
Starting curl command for query: tg_shortest_ss_pos_wt_tb on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_pos_wt_tb/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_pos_wt_tb/duration.txt
Finished curl command for query: tg_shortest_ss_pos_wt_tb on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_shortest_ss_pos_wt_tb/memory.txt
==================== path/tg_all_path run 0 ====================
Starting curl command for query: tg_all_path on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16973847.RESTPP_1_1.1720516966396.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/path/tg_all_path/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_all_path/duration.txt
Finished curl command for query: tg_all_path on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_all_path/memory.txt
==================== path/tg_msf run 0 ====================
Starting curl command for query: tg_msf on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16973851.RESTPP_1_1.1720517867862.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/path/tg_msf/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_msf/duration.txt
Finished curl command for query: tg_msf on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_msf/memory.txt
==================== path/tg_mst run 0 ====================
Starting curl command for query: tg_mst on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/path/tg_mst/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_mst/duration.txt
Finished curl command for query: tg_mst on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_mst/memory.txt
==================== path/tg_bfs run 0 ====================
Starting curl command for query: tg_bfs on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/path/tg_bfs/result.json
Duration has been written to /home/tigergraph/data/algos/path/tg_bfs/duration.txt
Finished curl command for query: tg_bfs on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/path/tg_bfs/memory.txt
==================== centrality/tg_closeness_cent_approx run 0 ====================
Starting curl command for query: tg_closeness_cent_approx on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16842784.RESTPP_1_1.1720518776855.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/centrality/tg_closeness_cent_approx/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_closeness_cent_approx/duration.txt
Finished curl command for query: tg_closeness_cent_approx on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_closeness_cent_approx/memory.txt
==================== centrality/tg_eigenvector_cent run 0 ====================
Starting curl command for query: tg_eigenvector_cent on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_eigenvector_cent/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_eigenvector_cent/duration.txt
Finished curl command for query: tg_eigenvector_cent on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_eigenvector_cent/memory.txt
==================== centrality/tg_influence_maximization_greedy run 0 ====================
Starting curl command for query: tg_influence_maximization_greedy on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_influence_maximization_greedy/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_influence_maximization_greedy/duration.txt
Finished curl command for query: tg_influence_maximization_greedy on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_influence_maximization_greedy/memory.txt
==================== centrality/tg_influence_maximization_CELF run 0 ====================
Starting curl command for query: tg_influence_maximization_CELF on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_influence_maximization_CELF/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_influence_maximization_CELF/duration.txt
Finished curl command for query: tg_influence_maximization_CELF on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_influence_maximization_CELF/memory.txt
==================== centrality/tg_degree_cent run 0 ====================
Starting curl command for query: tg_degree_cent on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_degree_cent/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_degree_cent/duration.txt
Finished curl command for query: tg_degree_cent on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_degree_cent/memory.txt
==================== centrality/tg_weighted_degree_cent run 0 ====================
Starting curl command for query: tg_weighted_degree_cent on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_weighted_degree_cent/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_weighted_degree_cent/duration.txt
Finished curl command for query: tg_weighted_degree_cent on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_weighted_degree_cent/memory.txt
==================== centrality/tg_pagerank run 0 ====================
Starting curl command for query: tg_pagerank on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_pagerank/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_pagerank/duration.txt
Finished curl command for query: tg_pagerank on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_pagerank/memory.txt
==================== centrality/tg_pagerank_wt run 0 ====================
Starting curl command for query: tg_pagerank_wt on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_wt/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_wt/duration.txt
Finished curl command for query: tg_pagerank_wt on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_wt/memory.txt
==================== centrality/tg_pagerank_pers run 0 ====================
Starting curl command for query: tg_pagerank_pers on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_pers/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_pers/duration.txt
Finished curl command for query: tg_pagerank_pers on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_pers/memory.txt
==================== centrality/tg_pagerank_pers_ap_batch run 0 ====================
Starting curl command for query: tg_pagerank_pers_ap_batch on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16842793.RESTPP_1_1.1720520220984.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_pers_ap_batch/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_pers_ap_batch/duration.txt
Finished curl command for query: tg_pagerank_pers_ap_batch on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_pagerank_pers_ap_batch/memory.txt
==================== centrality/tg_harmonic_cent run 0 ====================
Starting curl command for query: tg_harmonic_cent on graph: MyGraph
Error: The query didn't finish because it exceeded the query timeout threshold (900 seconds). Please check GSE log for license expiration and RESTPP/GPE log with request id (16842797.RESTPP_1_1.1720521122397.N) for details. Try increase header GSQL-TIMEOUT value.
Result has been written to /home/tigergraph/data/algos/centrality/tg_harmonic_cent/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_harmonic_cent/duration.txt
Finished curl command for query: tg_harmonic_cent on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_harmonic_cent/memory.txt
==================== centrality/tg_article_rank run 0 ====================
Starting curl command for query: tg_article_rank on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/centrality/tg_article_rank/result.json
Duration has been written to /home/tigergraph/data/algos/centrality/tg_article_rank/duration.txt
Finished curl command for query: tg_article_rank on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/centrality/tg_article_rank/memory.txt
```
