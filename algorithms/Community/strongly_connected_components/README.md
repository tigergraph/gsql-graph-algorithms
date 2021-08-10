# strongly_connected_components
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#strongly-connected-components-1
### Install strongly_connected_components via Tigergraph CLI
```bash
$ tg box algos install strongly_connected_components
```
### Install strongly_connected_components via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <strongly_connected_components_gsql_code>
$ END 
$ INSTALL QUERY strongly_connected_components
```
## strongly_connected_components Change Logs

### `tg_scc` Logs
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
### 2019-08-02 
	 fab713e : delete trim_end_iter
### 2019-08-02 
	 fb3ba39 : fix install script
### 2019-07-23 
	 e84fa48 : Update scc.gsql
### 2019-07-19 
	 f932b80 : update scc install
### 2019-07-17 
	 60a4916 : update install.sh
### 2019-07-16 
	 64ded1c : add scc
