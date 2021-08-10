# minimum_spanning_forest
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#minimum-spanning-forest-msf
### Install minimum_spanning_forest via Tigergraph CLI
```bash
$ tg box algos install minimum_spanning_forest
```
### Install minimum_spanning_forest via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <minimum_spanning_forest_gsql_code>
$ END 
$ INSTALL QUERY minimum_spanning_forest
```
## minimum_spanning_forest Change Logs

### `tg_msf` Logs
### 2021-07-23 
	 ac43583 : moved examples to template and updated query names
### 2021-07-13 
	 f37701b : more descriptive naming convention
### 2021-07-13 
	 2170f21 : dash to underscore
### 2021-07-13 
	 ec58568 : New schema-free layout
### 2020-09-28 
	 d65fc07 : standard parameters: msf,scc,pageRank_pers,pageRank_wt
### 2020-09-18 
	 14d3d6b : add 3.0 branch
### 2020-08-13 
	 1da86dc : Schema Less Queries
### 2020-03-16 
	 da4a2fd : Create msf.gtmp
### 2019-11-04 
	 537c478 : update wcc
### 2019-08-22 
	 6c9e5c2 : bugfix: no more double-counting edges on two-vertex cycles
### 2019-08-20 
	 31d94c1 : fixed install script algorithm name match + edge weight attribute substitution
### 2019-08-20 
	 be35357 : remove max_iter parameter for MSF
### 2019-08-19 
	 52d7b9c : minimum spanning forest template and install script
