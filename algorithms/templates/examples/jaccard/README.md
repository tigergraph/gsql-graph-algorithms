# jaccard
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#jaccard-similarity-of-neighborhoods-batch
### Install jaccard via Tigergraph CLI
```bash
$ tg box algos install jaccard
```
### Install jaccard via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <jaccard_gsql_code>
$ END 
$ INSTALL QUERY jaccard
```
## jaccard Change Logs

### `movie_jaccard_nbor_ap_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"0af113a   Suxiaocai   Tue Mar 12 23:24:36 2019 +0000   [GF-1028]fix Closeness Centrality"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"e7f77af   Suxiaocai    Fri Feb 1 23:17:31 2019 +0000   fix test graph install and Jaccard topK"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
```

### `movie_jaccard_nbor_ss_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
```

### `movie_jaccard_nbor_ss` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
```

### `movie_jaccard_nbor_ss_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"e2fda3f   Suxiaocai   Fri Apr 12 23:49:32 2019 +0000   add jaccard_ss, update cosine_ss"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
```

### `movie_jaccard_nbor_ap` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"e7f77af   Suxiaocai    Fri Feb 1 23:17:31 2019 +0000   fix test graph install and Jaccard topK"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
```

### `movie_jaccard_nbor_ap_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"e7f77af   Suxiaocai    Fri Feb 1 23:17:31 2019 +0000   fix test graph install and Jaccard topK"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
```
