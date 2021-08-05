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

### `tg_closeness_cent` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"99a6853   Yiming Pan  Tue Jun 22 13:32:06 2021 -0400   Update closeness_cent.gsql"
"5405380   Yiming Pan  Tue Jun 22 13:09:28 2021 -0400   Update closeness_cent.gsql"
"e158ae7   Yiming Pan  Tue Jun 22 12:48:15 2021 -0400   Rename MScloseness_cent.gsql to closeness_cent.gsql"
"869bdaa   Yiming Pan  Mon Jun 21 18:12:25 2021 -0400   Update MScloseness_cent.gsql"
"d8a3713   Yiming Pan  Mon Jun 21 18:02:08 2021 -0400   Update MScloseness_cent.gsql"
"d516f1b   Yiming Pan  Mon Jun 21 18:01:49 2021 -0400   Update MScloseness_cent.gsql"
"c65ad50   Yiming Pan  Thu Jun 17 14:44:38 2021 -0400   Update bc,cc,cc_approx,add cycle-detection-count,LCC"
"3c59bfe   Yiming Pan  Thu Jun 17 14:42:38 2021 -0400   Delete MScloseness_cent.gsql"
"0f5a3f5   Yiming Pan  Thu Jun 17 14:38:57 2021 -0400   Add files via upload"
"d77347c   Yiming Pan  Tue May 25 13:34:29 2021 -0400   Add lcc, cc and cc_aprox"
```

### `tg_closeness_cent_approx` Logs

```
"ac43583   WilliamH3O  Fri Jul 23 11:58:00 2021 -0700   moved examples to template and updated query names"
"f37701b   WilliamH3O  Tue Jul 13 15:47:02 2021 -0700   more descriptive naming convention"
"ec58568   WilliamH3O  Tue Jul 13 12:03:54 2021 -0700   New schema-free layout"
"8581447   Yiming Pan  Mon Jun 21 18:03:58 2021 -0400   Rename MScloseness_cent_approx.gsql to closeness_cent_approx_query.gsql"
"34b7696   Yiming Pan  Mon Jun 21 18:02:56 2021 -0400   Update MScloseness_cent_approx.gsql"
"e946c0e   Yiming Pan  Mon Jun 21 17:55:57 2021 -0400   Update MScloseness_cent_approx.gsql"
"7fa30ac   Yiming Pan  Fri Jun 18 12:44:17 2021 -0400   Update MScloseness_cent_approx.gsql"
"c65ad50   Yiming Pan  Thu Jun 17 14:44:38 2021 -0400   Update bc,cc,cc_approx,add cycle-detection-count,LCC"
"0808f29   Yiming Pan  Thu Jun 17 14:42:34 2021 -0400   Delete MScloseness_cent_approx.gsql"
"58a70b2   Yiming Pan  Thu Jun 17 14:41:45 2021 -0400   Add files via upload"
```
