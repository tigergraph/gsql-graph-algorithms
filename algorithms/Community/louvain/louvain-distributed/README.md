### louvain-distributed
This algorithm requires user defined function (UDF).
UDFs are defined in `ExprFunctions.hpp`, use the instruction below for installation.

Load ExprFunctions to TigerGraph:
```
gsql 'PUT ExprFunctions FROM "ExprFunctions.hpp"'
```

Restart TigerGraph:
```
gadmin restart all
```

For more information about UDF, reference the documentation page [here](https://docs.tigergraph.com/dev/gsql-ref/querying/operators-functions-and-expressions#query-user-defined-functions).

Aftern installing UDF, you can run the algorithm:
```
gsql louvain_distributed_query.gsql
```