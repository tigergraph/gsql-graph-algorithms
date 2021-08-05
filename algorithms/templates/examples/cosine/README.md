# cosine
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#cosine-similarity-of-neighborhoods-batch
### Install cosine via Tigergraph CLI
```bash
$ tg box algos install cosine
```
### Install cosine via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <cosine_gsql_code>
$ END 
$ INSTALL QUERY cosine
```
## cosine Change Logs

### `movie_cosine_nbor_ap_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"279bdc2   Suxiaocai   Thu Dec 20 18:45:23 2018 +0000   fixed indentation"
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
```

### `movie_cosine_nbor_ap` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"279bdc2   Suxiaocai   Thu Dec 20 18:45:23 2018 +0000   fixed indentation"
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
```

### `movie_cosine_nbor_ap_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"279bdc2   Suxiaocai   Thu Dec 20 18:45:23 2018 +0000   fixed indentation"
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
"3bd2cf1   Suxiaocai   Tue Dec 11 23:49:53 2018 +0000   update    "
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
```

### `movie_cosine_nbor_ss` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"5f3836d   TigerGraph User  Tue Jun 25 23:24:45 2019 +0000   revise for pull request#3"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"a06dcf8   Suxiaocai    Thu May 9 21:14:26 2019 +0000   add knn   "
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"67ee267   Suxiaocai   Mon Feb 11 18:41:45 2019 +0000   fix test data"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
"3bd2cf1   Suxiaocai   Tue Dec 11 23:49:53 2018 +0000   update    "
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
```

### `movie_cosine_nbor_ss_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"5f3836d   TigerGraph User  Tue Jun 25 23:24:45 2019 +0000   revise for pull request#3"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"a06dcf8   Suxiaocai    Thu May 9 21:14:26 2019 +0000   add knn   "
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
```

### `movie_cosine_nbor_ss_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"5f3836d   TigerGraph User  Tue Jun 25 23:24:45 2019 +0000   revise for pull request#3"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"a06dcf8   Suxiaocai    Thu May 9 21:14:26 2019 +0000   add knn   "
"bf92e45   Suxiaocai   Thu Feb 14 03:10:25 2019 +0000   revise similarity algos, change topK logic"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"ae35bd2   Suxiaocai   Thu Dec 20 18:38:53 2018 +0000   changed names, added install all choice"
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"379d0f7   Suxiaocai   Thu Dec 13 01:34:25 2018 +0000   change jaccard to gtmp, revise install.sh"
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
```
