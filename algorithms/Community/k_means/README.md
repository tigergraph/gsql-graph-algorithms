# k_means
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#https://raw.githubusercontent.com/tigergraph/gsql-graph-algorithms/master/algorithms/schema-free/kmeans.gsql
### Install k_means via Tigergraph CLI
```bash
$ tg box algos install k_means
```
### Install k_means via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <k_means_gsql_code>
$ END 
$ INSTALL QUERY k_means
```
## k_means Change Logs

### `tg_kmeans_sub` Logs
### 2021-07-23 
	 ac43583 : moved examples to template and updated query names
### 2021-07-16 
	 15849ea : add tg prefixes
### 2021-07-13 
	 2170f21 : dash to underscore
### 2021-07-13 
	 ec58568 : New schema-free layout
### 2021-01-16 
	 4df197d : PR updates
### 2021-01-07 
	 6606a3a : jaccard/cosine update, kmeans in progress
### 2021-01-05 
	 5c761ec : kmeans/jaccard/cosine/closenss_cent_approx

### `tg_kmeans` Logs
### 2021-07-23 
	 ac43583 : moved examples to template and updated query names
### 2021-07-19 
	 a5ef77e : fix tg prefix for some dependencies
### 2021-07-16 
	 4c5f65d : add tg prefix to kmeans dependency
### 2021-07-13 
	 f37701b : more descriptive naming convention
### 2021-07-13 
	 2170f21 : dash to underscore
### 2021-07-13 
	 ec58568 : New schema-free layout
### 2021-01-16 
	 4df197d : PR updates
### 2021-01-07 
	 6606a3a : jaccard/cosine update, kmeans in progress
### 2021-01-05 
	 5c761ec : kmeans/jaccard/cosine/closenss_cent_approx
