# FastRP

## Available FastRP Algorithms 

* [`tg_fastRP`](https://github.com/tigergraph/gsql-graph-algorithms/blob/github_link_fix/algorithms/GraphML/FastRP/tg_fastRP.gsql)


## Instructions

### Preliminary Notes
**  Vim is the text editor of choice in this README, any other text editors such as Emacs or Nano will suffice in the commands listed below 
\
**  `<TGversion>` should be replaced with your current Tigergraph version number


### Getting UDF
`extract_list()` and `fastrp_rand_func()` are user-defined functions utilized in `tg_fastRP.gsql` \
The code defined in `tg_fastRP.cpp` should be pasted inside the `UDIMPL` namespace inside of `ExprFunctions.hpp`. Be sure to also paste the proper `include` statements at the top of the `ExprFunctions.hpp`
```bash
# open file and paste code

$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp
```

### Multiple machines(cluster) or Single Machine?
If the data is on a single machine, proceed to the next section.
\
If the data is spread across multiple machines, include the `DISTRIBUTED` GSQL keyword in the header of the `tg_fastRP` query 
```bash
# Change first header to the second header

CREATE QUERY tg_fastRP_query(...) {...}         
CREATE DISTRIBUTED QUERY tg_fastRP_query(...) {...}
```

If you are on multiple machines or a cluster, do the following `PUT` command in every machine
```bash
# For every machine in cluster  

$ gssh <machine>
$ PUT ExprFunctions from "/home/tigergraph/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp"
```

### Running Queries
The following instructions can be done with GraphStudio or GSQL terminal:
1. Install the `tg_fastRP` query - **Note:** There are hard-coded parameters in the query, primarily in the ```@embedding_arr``` and ```@final_embedding_arr``` accumulators. Please change the size of these arrays to the desired dimension. Furthermore, the query assumes there is an ```LIST<FLOAT>``` attribute on every vertex with the name `fastrp_embedding`. If this is not the case, please change the query accordingly.
2. Run query `tg_fastRP`. Parameters following notation names defined in the original research paper : https://arxiv.org/pdf/1908.11512.pdf
