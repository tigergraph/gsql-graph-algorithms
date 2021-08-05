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

### `PR_pageRank_wt_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"e630c4c   Suxiaocai   Sat Jan 19 01:44:24 2019 +0000   add weighted PR"
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"3bd2cf1   Suxiaocai   Tue Dec 11 23:49:53 2018 +0000   update    "
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_pageRank_pers_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"479ce99   Suxiaocai   Fri Apr 26 00:31:42 2019 +0000   update examples"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"80a3db4   Suxiaocai   Thu Jan 17 02:21:48 2019 +0000   Add PPR   "
```

### `social_pageRank_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_pageRank_wt` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"e630c4c   Suxiaocai   Sat Jan 19 01:44:24 2019 +0000   add weighted PR"
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_pageRank_pers` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"479ce99   Suxiaocai   Fri Apr 26 00:31:42 2019 +0000   update examples"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"80a3db4   Suxiaocai   Thu Jan 17 02:21:48 2019 +0000   Add PPR   "
```

### `social_pageRank` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"b84eeac   Suxiaocai   Thu Mar 14 18:00:28 2019 +0000   add&test distributed, add test example for MST"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `PR_pageRank_wt_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"e630c4c   Suxiaocai   Sat Jan 19 01:44:24 2019 +0000   add weighted PR"
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_pageRank_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"b84eeac   Suxiaocai   Thu Mar 14 18:00:28 2019 +0000   add&test distributed, add test example for MST"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"3bd2cf1   Suxiaocai   Tue Dec 11 23:49:53 2018 +0000   update    "
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_pageRank_pers_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"479ce99   Suxiaocai   Fri Apr 26 00:31:42 2019 +0000   update examples"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"f39b4b5   Suxiaocai   Thu Jan 17 20:10:13 2019 +0000   delete counter for iteration in pageRank"
"80a3db4   Suxiaocai   Thu Jan 17 02:21:48 2019 +0000   Add PPR   "
```
