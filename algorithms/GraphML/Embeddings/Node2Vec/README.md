# Node2Vec
## Instructions

### Preliminary Notes
**  Vim is the text editor of choice in this README, any other text editors such as Emacs or Nano will suffice in the commands listed below 
\
**  `<TGversion>` should be replaced with your current Tigergraph version number

### Getting UDF
`node2vec()` is a user-defined function utilized in `node2vec_query.gsql` \
**The code defined in `UDF` should be pasted inside the `UDIMPL` namespace inside of `ExprFunctions.hpp`
```bash
# open file and paste code

$ vim ~/tigergraph/app/<TGversion>/dev/gdk/gsql/src/QueryUdf/ExprFunctions.hpp
```

### Getting Word2vec file
There are multiple options to get `word2vec.h`
1. Download/Copy `word2vec.h` file into `~/tigergraph/app/<TGversion>/dev/gdk/gsdk/include` directory
2. Create the file and copy the code from `word2vec.h` and paste it into the newly created file (steps shown below)
```bash
# Go to correct directory
$ cd ~/tigergraph/app/<TGversion>/dev/gdk/gsdk/include/

# create file and paste code
$ vim word2vec.h                  
```

### Including word2vec
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
2. Run query `random_walk` with desired parameters. Visit https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#parameters for a description of the random walk query parameters
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
