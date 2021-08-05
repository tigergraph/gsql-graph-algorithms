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

### `social_shortest_ss_pos_wt` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"cdaafd9   Suxiaocai   Wed Jan 15 23:11:23 2020 +0000   update SSSP wt"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"0af113a   Suxiaocai   Tue Mar 12 23:24:36 2019 +0000   [GF-1028]fix Closeness Centrality"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
```

### `generic_shortest_ss_no_wt_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
```

### `generic_shortest_ss_no_wt_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
```

### `social_shortest_ss_no_wt` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"b84eeac   Suxiaocai   Thu Mar 14 18:00:28 2019 +0000   add&test distributed, add test example for MST"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"ddbb2e3   Suxiaocai   Fri Dec 14 21:40:00 2018 +0000   change display choice"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
```

### `social_shortest_ss_any_wt_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"ce3816f   Suxiaocai   Fri Jan 17 00:28:37 2020 +0000   add exception"
"cdaafd9   Suxiaocai   Wed Jan 15 23:11:23 2020 +0000   update SSSP wt"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_shortest_ss_any_wt` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"ce3816f   Suxiaocai   Fri Jan 17 00:28:37 2020 +0000   add exception"
"cdaafd9   Suxiaocai   Wed Jan 15 23:11:23 2020 +0000   update SSSP wt"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_shortest_ss_pos_wt_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"cdaafd9   Suxiaocai   Wed Jan 15 23:11:23 2020 +0000   update SSSP wt"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
```

### `work_shortest_sp_pos_wt` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"cc624c3   Suxiaocai   Wed Apr 24 21:45:00 2019 +0000   fix typo  "
```

### `social_shortest_ss_any_wt_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"ce3816f   Suxiaocai   Fri Jan 17 00:28:37 2020 +0000   add exception"
"cdaafd9   Suxiaocai   Wed Jan 15 23:11:23 2020 +0000   update SSSP wt"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_shortest_ss_pos_wt_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"2170f21   WilliamH3O  Tue Jul 13 14:31:49 2021 -0700   dash to underscore"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"cdaafd9   Suxiaocai   Wed Jan 15 23:11:23 2020 +0000   update SSSP wt"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"c511113   Suxiaocai   Fri Dec 14 20:13:25 2018 +0000   revise install_free"
"7d895bb   Suxiaocai   Wed Nov 21 01:06:15 2018 +0000   add 2 shortest path queries"
```
