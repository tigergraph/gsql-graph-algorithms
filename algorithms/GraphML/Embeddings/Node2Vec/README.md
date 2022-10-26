# Node2Vec

Node2Vec is a vertex embedding algorithm proposed in [node2vec: Scalable Feature Learning for Networks](https://arxiv.org/abs/1607.00653?context=cs). TigerGraph splits the computation into two parts: the random walk process and the embedding training process. Assuming that you are using version 3.6 or greater of the TigerGraph database, ignore the UDF install instructions.

## [TigerGraph Node2Vec Documentation](https://docs.tigergraph.com/graph-ml/current/node-embeddings/node2vec)

## Instructions

### Random Walk Process Install
There are two different random walk processes to choose from. The first is regular random walks, implemented in `tg_random_walk.gsql`. This is equivalent to setting `p` and `q` parameters of Node2Vec both to 1, which is also equivalent to the [DeepWalk](https://arxiv.org/pdf/1403.6652.pdf) paper. This version is more performant than `tg_weighted_random_walk.gsql`, due to the less computation that is needed. If the graph is large, you may want to batch the random walk process to reduce memory consumption. Use `tg_random_walk_batch.gsql` if this is desired.

The second option is weighted random walk, as described in the Node2Vec paper. This is implemented in the `tg_weighted_random_walk_sub.gsql` and `tg_weighted_random_walk.gsql`. If your TigerGraph database version is below 3.6, see the UDF installation instructions below. If the graph is large, you may want to batch the random walk process to reduce memory consumption. Use `tg_weighted_random_walk_batch.gsql` with `tg_weighted_random_walk_sub.gsql` if desired.

**To install the un-weighted random walk:** copy the algorithm from `tg_random_walk.gsql` and install it on the database using the standard query install process.

**To install the weighted random walk:** copy `tg_weighted_random_walk_sub.gsql` and install. Then copy and install `tg_weighted_random_walk.gsql`.

### Node2Vec Embedding Install
Once the random walks have been generated, we can use the output to train the Node2Vec model. To install, make sure the proper UDFs are installed. If you are using a TigerGraph database of version 3.6 or greater, the UDFs are pre-installed.

**To install Node2Vec query:** copy the query from `tg_node2vec.gsql` and install on the database.

### Preliminary Notes
Vim is the text editor of choice in this README, any other text editors such as Emacs or Nano will suffice in the commands listed below 
\
`<TGversion>` should be replaced with your current Tigergraph version number

### UDF installation

#### Weighted Random Walk UDF install
If you are using `tg_weighted_random_walk_sub.gsql`, then you will need to install the `tg_random_udf.cpp`. **The code defined in `tg_random_udf.cpp` should be pasted inside the `UDIMPL`f namespace inside of `ExprFunctions.hpp`.
```bash
# open file and paste code

$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp
```

#### Node2Vec UDF install
`tg_node2vec_sub()` is a UDF that is called in `tg_node2vec.gsql`. \
**The code defined in `tg_node2vec_sub.cpp` should be pasted inside the `UDIMPL` namespace inside of `ExprFunctions.hpp`
```bash
# open file and paste code

$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp
```

##### Getting Word2vec file
There are multiple options to get `word2vec.h`
1. Download/Copy `word2vec.h` file into `~/tigergraph/app/<TGversion>/dev/gdk/gsdk/include` directory
2. Create the file and copy the code from `word2vec.h` and paste it into the newly created file (steps shown below)
```bash
# Go to correct directory
$ cd ~/tigergraph/app/<TGversion>/dev/gdk/gsdk/include/

# create file and paste code
$ vim word2vec.h                  
```

##### Including word2vec
The newly created `word2vec.h` needs to be included in the `ExprUtil.hpp` file
```bash
$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprUtil.hpp
```
Once inside the text editor, paste the following line of `C++` code into under the other include statements 
```c++
#include "/home/tigergraph/tigergraph/app/<TGversion>/dev/gdk/gsdk/include/word2vec.h"
```
### Multiple machines(cluster) or Single Machine?
If you are working on a single machine, remove the `Distributed` GSQL keyword from the header of the `random_walk` query 
```bash
# Change first header to the second header

CREATE DISTRIBUTED QUERY random_walk(...) {...}         
CREATE QUERY random_walk(...) {...}
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
1. Install the `random_walk` query
2. Run query `random_walk` with desired parameters. Visit https://docs.tigergraph.com/graph-ml/current/node-embeddings/node2vec for a description of the random walk query parameters. Make sure that TigerGraph has the correct permissions to write to the output directory you specify.
3. (optional) Inspect output of random_walk query
    ```bash
    # For the default filepath parameter

    $ cat ~/path.csv
    ```
4. Run `node2vec_query` with desired parameters. `Dimension` denotes the embedding dimension size
5. (optional) Inspect Embeddings
    ```bash
    # For the default filepath parameter

    $ cat ~/embedding.csv
    ```
