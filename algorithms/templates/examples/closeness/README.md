# closeness
## Documentation : https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#closeness-centrality
### Install closeness via Tigergraph CLI
```bash
$ tg box algos install closeness
```
### Install closeness via GSQL terminal
```bash
$ BEGIN 

# Paste query code after BEGIN command

$ <closeness_gsql_code>
$ END 
$ INSTALL QUERY closeness
```
## closeness Change Logs

### `social_closeness_cent_tmp` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"6d20d1a   Suxiaocai   Wed Mar 13 07:11:58 2019 +0000   [GF945]Add batch mode choice"
"0af113a   Suxiaocai   Tue Mar 12 23:24:36 2019 +0000   [GF-1028]fix Closeness Centrality"
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"ddbb2e3   Suxiaocai   Fri Dec 14 21:40:00 2018 +0000   change display choice"
"39752dd   Suxiaocai   Fri Dec 14 19:25:21 2018 +0000   fixed all indentation and key words"
"946b08a   Suxiaocai   Fri Dec 14 01:53:40 2018 +0000   change VSET logic, delete path choice, fix indentation"
"aaf2de4   Suxiaocai   Fri Nov 30 18:30:02 2018 +0000   add similarity algo and revised install.sh"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_closeness_cent_attr` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"0af113a   Suxiaocai   Tue Mar 12 23:24:36 2019 +0000   [GF-1028]fix Closeness Centrality"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_closeness_cent_file` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"0af113a   Suxiaocai   Tue Mar 12 23:24:36 2019 +0000   [GF-1028]fix Closeness Centrality"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```

### `social_closeness_cent` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"245f462   Suxiaocai   Thu May 16 20:04:37 2019 +0000   finish up knn cv template"
"0af113a   Suxiaocai   Tue Mar 12 23:24:36 2019 +0000   [GF-1028]fix Closeness Centrality"
"c5530eb   Suxiaocai   Tue Jan 29 22:25:10 2019 +0000   add plmr  "
"0b60b48   Suxiaocai   Tue Jan 15 19:12:59 2019 +0000   Added topK for similarity ATTR version. Revised names."
"9c78d4e   Suxiaocai   Sat Dec 15 01:36:41 2018 +0000   fixed format issues, regenerated .gsql files, updated README"
"5373c48   Heqing Ya   Fri Oct 26 15:07:48 2018 -0700   Add graph algorithms"
```
