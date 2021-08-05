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

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"d65fc07   Victor Lee  Mon Sep 28 05:29:44 2020 -0400   standard parameters: msf,scc,pageRank_pers,pageRank_wt"
"14d3d6b   Victor Lee  Fri Sep 18 02:17:18 2020 -0400   add 3.0 branch"
"1da86dc   Ramko9999   Thu Aug 13 14:50:04 2020 -0700   Schema Less Queries"
"da4a2fd   rkahhaleh   Mon Mar 16 12:09:18 2020 -0700   Create msf.gtmp"
"537c478   TigerGraph User   Mon Nov 4 17:41:19 2019 +0000   update wcc"
"6c9e5c2   Jerry Chen  Thu Aug 22 17:59:00 2019 -0700   bugfix: no more double-counting edges on two-vertex cycles"
"31d94c1   Jerry Chen  Tue Aug 20 10:38:48 2019 -0700   fixed install script algorithm name match + edge weight attribute substitution"
"be35357   Jerry Chen  Tue Aug 20 09:44:56 2019 -0700   remove max_iter parameter for MSF"
"52d7b9c   Jerry Chen  Mon Aug 19 14:50:12 2019 -0700   minimum spanning forest template and install script"
```
