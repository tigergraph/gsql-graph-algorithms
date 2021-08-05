# pagerank
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#pagerank
### Install pagerank via Tigergraph CLI
```bash
$ tg box algos install pagerank
```
### Install pagerank via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <pagerank_gsql_code>
$ END 
$ INSTALL QUERY pagerank
```
## pagerank Change Logs

### `tg_pageRank_pers` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"d65fc07   Victor Lee  Mon Sep 28 05:29:44 2020 -0400   standard parameters: msf,scc,pageRank_pers,pageRank_wt"
"14d3d6b   Victor Lee  Fri Sep 18 02:17:18 2020 -0400   add 3.0 branch"
"1da86dc   Ramko9999   Thu Aug 13 14:50:04 2020 -0700   Schema Less Queries"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"479ce99   Suxiaocai   Fri Apr 26 00:31:42 2019 +0000   update examples"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"80a3db4   Suxiaocai   Thu Jan 17 02:21:48 2019 +0000   Add PPR   "
```

### `tg_pageRank_wt` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"d65fc07   Victor Lee  Mon Sep 28 05:29:44 2020 -0400   standard parameters: msf,scc,pageRank_pers,pageRank_wt"
"14d3d6b   Victor Lee  Fri Sep 18 02:17:18 2020 -0400   add 3.0 branch"
"bb48267   Ramko9999   Wed Aug 19 10:52:24 2020 -0700   Fixed writing to file problems"
"1da86dc   Ramko9999   Thu Aug 13 14:50:04 2020 -0700   Schema Less Queries"
```

### `tg_pageRank` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"a816887   Victor Lee  Wed Sep 23 01:49:35 2020 -0400   fix pageRank, more standardized elsewhere"
"54e697a   Victor Lee  Tue Sep 22 15:36:30 2020 -0400   standardize 1st batch of algorithms"
"14d3d6b   Victor Lee  Fri Sep 18 02:17:18 2020 -0400   add 3.0 branch"
"bb48267   Ramko9999   Wed Aug 19 10:52:24 2020 -0700   Fixed writing to file problems"
"1da86dc   Ramko9999   Thu Aug 13 14:50:04 2020 -0700   Schema Less Queries"
```
