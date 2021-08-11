# FastRP
## Instructions

### Preliminary Notes
**  Vim is the text editor of choice in this README, any other text editors such as Emacs or Nano will suffice in the commands listed below 
\
**  `<TGversion>` should be replaced with your current Tigergraph version number

### Getting Eigen
`Eigen` is a software utilized in this algorithm under the MPL2 License. We need to clone the software and move it to the Tigergraph thirdparty directory
```bash
$ cd
$ git clone https://gitlab.com/libeigen/eigen.git
$ mv eigen /home/tigergraph/tigergraph/app/<TGversion>/dev/gdk/gsdk/include/thirdparty
```


### Getting UDF
`fastRP()` is a user-defined function utilized in `tg_fastRP_query.gsql` \
**The code defined in `fastRP.cpp` should be pasted inside the `UDIMPL` namespace inside of `ExprFunctions.hpp`
```bash
# open file and paste code

$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp
```

### Including Eigen
It is important to include directives utilized by the UDF inside the `ExprUtil.hpp` file
```bash
$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprUtil.hpp
```
Once inside the text editor, paste the following line of `C++` code into under the other include statements 
```c++
#include "/home/tigergraph/tigergraph/app/<TGversion>/dev/gdk/gsdk/include/thirdparty/eigen/Eigen/SparseCore"

using Eigen::Triplet;
using Eigen::SparseMatrix;
```

### Multiple machines(cluster) or Single Machine?
If you are working on a single machine, include the `Distributed` GSQL keyword in the header of the `tg_fastRP_query` query 
```bash
# Change first header to the second header

CREATE QUERY tg_fastRP_query(...) {...}         
CREATE DISTRIBUTED QUERY tg_fastRP_query(...) {...}
```
After doing this, proceed to the next section(Running Queries)

If you are on multiple machines or a cluster
```bash
# For every machine in cluster  

$ gssh <machine>
$ PUT ExprFunctions from "/home/tigergraph/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp"
```

### Running Queries
** The following instructions can be done with GraphStudio or GSQL terminal
1. Install the `tg_fastRP_query` query
2. Run query `tg_fastRP_query` with desired parameters. Parameters following notation names defined in the original research paper : https://arxiv.org/pdf/1908.11512.pdf
3. (optional) Inspect output of random_walk query

```bash
# For the default filepath parameter

$ cat ~/parameters.txt
```