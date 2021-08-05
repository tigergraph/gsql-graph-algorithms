# k_nearest_neighbors
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#k-nearest-neighbors-cosine-neighbor-similarity-all-vertices-batch
### Install k_nearest_neighbors via Tigergraph CLI
```bash
$ tg box algos install k_nearest_neighbors
```
### Install k_nearest_neighbors via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <k_nearest_neighbors_gsql_code>
$ END 
$ INSTALL QUERY k_nearest_neighbors
```
## k_nearest_neighbors Change Logs

### `movie_knn_cosine_all` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
```

### `movie_knn_cosine_all_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
```

### `movie_knn_cosine_ss` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
"8cc6900   Elena Su    Tue Jul 23 11:56:07 2019 -0700   Delete knn_cosine_ss.gsql"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"9f8a5ba   TigerGraph User  Tue Jun 25 23:26:34 2019 +0000   add generated dir"
"5f3836d   TigerGraph User  Tue Jun 25 23:24:45 2019 +0000   revise for pull request#3"
"38937af   TigerGraph User  Tue Jun 25 21:45:33 2019 +0000   revise query comment"
"371beed   TigerGraph User  Mon Jun 24 21:36:46 2019 +0000   delete general similarity"
"95097ac   Suxiaocai   Thu May 16 20:05:56 2019 +0000   add knn examples"
"e782e28   Suxiaocai   Sat May 11 01:21:26 2019 +0000   fix knn_cosine label"
"d034435   Suxiaocai   Fri May 10 03:32:11 2019 +0000   finish knn_cosine"
"a06dcf8   Suxiaocai    Thu May 9 21:14:26 2019 +0000   add knn   "
```

### `movie_knn_cosine_ss_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
"3890ebd   Elena Su    Tue Jul 23 11:56:18 2019 -0700   Delete knn_cosine_ss_attr.gsql"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"9f8a5ba   TigerGraph User  Tue Jun 25 23:26:34 2019 +0000   add generated dir"
"5f3836d   TigerGraph User  Tue Jun 25 23:24:45 2019 +0000   revise for pull request#3"
"38937af   TigerGraph User  Tue Jun 25 21:45:33 2019 +0000   revise query comment"
"371beed   TigerGraph User  Mon Jun 24 21:36:46 2019 +0000   delete general similarity"
"95097ac   Suxiaocai   Thu May 16 20:05:56 2019 +0000   add knn examples"
"e782e28   Suxiaocai   Sat May 11 01:21:26 2019 +0000   fix knn_cosine label"
"d034435   Suxiaocai   Fri May 10 03:32:11 2019 +0000   finish knn_cosine"
"a06dcf8   Suxiaocai    Thu May 9 21:14:26 2019 +0000   add knn   "
```

### `movie_knn_cosine_all_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
```

### `movie_knn_cosine_cv` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
"566773b   TigerGraph User   Thu Sep 5 18:10:36 2019 +0000   change names"
"b0af3ac   TigerGraph User   Thu Aug 1 18:05:32 2019 +0000   fix knn_cv"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"56019cf   TigerGraph User  Tue Jun 25 21:23:39 2019 +0000   delete knn_cosine_all and cv"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
```

### `movie_knn_cosine_ss_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"e5a5ddf   TigerGraph User   Thu Sep 5 18:45:17 2019 +0000   generate examples"
"307fdcd   Elena Su    Tue Jul 23 11:56:30 2019 -0700   Delete knn_cosine_ss_file.gsql"
"05664ba   TigerGraph User  Thu Jul 18 00:56:58 2019 +0000   update knn"
"9f8a5ba   TigerGraph User  Tue Jun 25 23:26:34 2019 +0000   add generated dir"
"5f3836d   TigerGraph User  Tue Jun 25 23:24:45 2019 +0000   revise for pull request#3"
"38937af   TigerGraph User  Tue Jun 25 21:45:33 2019 +0000   revise query comment"
"371beed   TigerGraph User  Mon Jun 24 21:36:46 2019 +0000   delete general similarity"
"95097ac   Suxiaocai   Thu May 16 20:05:56 2019 +0000   add knn examples"
"e782e28   Suxiaocai   Sat May 11 01:21:26 2019 +0000   fix knn_cosine label"
"d034435   Suxiaocai   Fri May 10 03:32:11 2019 +0000   finish knn_cosine"
"a06dcf8   Suxiaocai    Thu May 9 21:14:26 2019 +0000   add knn   "
```
