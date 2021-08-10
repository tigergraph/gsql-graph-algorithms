# shortest_path
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#single-source-shortest-path-weighted
### Install shortest_path via Tigergraph CLI
```bash
$ tg box algos install shortest_path
```
### Install shortest_path via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <shortest_path_gsql_code>
$ END 
$ INSTALL QUERY shortest_path
```
## shortest_path Change Logs

### `tg_shortest_ss_any_wt` Logs
### 2021-07-23 
	 ac43583 : moved examples to template and updated query names
### 2021-07-13 
	 f37701b : more descriptive naming convention
### 2021-07-13 
	 2170f21 : dash to underscore
### 2021-07-13 
	 ec58568 : New schema-free layout
### 2020-09-25 
	 1007534 : fix closeness_cent & shortest_ss_pos_wt
### 2020-09-22 
	 54e697a : standardize 1st batch of algorithms
### 2020-09-21 
	 ee2b9d4 : move louvain_parallel to schema-first
### 2020-09-18 
	 14d3d6b : add 3.0 branch
### 2020-08-13 
	 1da86dc : Schema Less Queries

### `tg_shortest_ss_pos_wt` Logs
### 2021-07-23 
	 ac43583 : moved examples to template and updated query names
### 2021-07-13 
	 f37701b : more descriptive naming convention
### 2021-07-13 
	 2170f21 : dash to underscore
### 2021-07-13 
	 ec58568 : New schema-free layout
### 2020-09-25 
	 1007534 : fix closeness_cent & shortest_ss_pos_wt
### 2020-09-23 
	 a816887 : fix pageRank, more standardized elsewhere
### 2020-09-22 
	 54e697a : standardize 1st batch of algorithms
### 2020-09-21 
	 ee2b9d4 : move louvain_parallel to schema-first
### 2020-09-18 
	 14d3d6b : add 3.0 branch
### 2020-08-13 
	 1da86dc : Schema Less Queries
### 2020-01-15 
	 cdaafd9 : update SSSP wt
### 2019-05-16 
	 245f462 : finish up knn cv template
### 2019-03-12 
	 0af113a : [GF-1028]fix Closeness Centrality
### 2019-01-29 
	 c5530eb : add plmr
### 2019-01-15 
	 0b60b48 : Added topK for similarity ATTR version. Revised names.
### 2018-12-15 
	 9c78d4e : fixed format issues, regenerated .gsql files, updated README
### 2018-12-14 
	 c511113 : revise install_free
### 2018-11-21 
	 7d895bb : add 2 shortest path queries

### `tg_shortest_ss_no_wt` Logs
### 2021-07-23 
	 ac43583 : moved examples to template and updated query names
### 2021-07-13 
	 f37701b : more descriptive naming convention
### 2021-07-13 
	 2170f21 : dash to underscore
### 2021-07-13 
	 ec58568 : New schema-free layout
### 2020-09-22 
	 54e697a : standardize 1st batch of algorithms
### 2020-09-21 
	 ee2b9d4 : move louvain_parallel to schema-first
### 2020-09-18 
	 14d3d6b : add 3.0 branch
### 2020-08-19 
	 bb48267 : Fixed writing to file problems
### 2020-08-13 
	 1da86dc : Schema Less Queries
### 2019-05-16 
	 245f462 : finish up knn cv template
### 2019-03-14 
	 b84eeac : add&test distributed, add test example for MST
### 2019-01-29 
	 c5530eb : add plmr
### 2019-01-15 
	 0b60b48 : Added topK for similarity ATTR version. Revised names.
### 2018-12-15 
	 9c78d4e : fixed format issues, regenerated .gsql files, updated README
### 2018-12-14 
	 ddbb2e3 : change display choice
### 2018-12-14 
	 c511113 : revise install_free
### 2018-11-21 
	 7d895bb : add 2 shortest path queries
