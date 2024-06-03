# Contribution Guidelines for Adding Tests

### Contents

- [Running the tests](#running-the-tests)
- [Directory Layout](#directory-layout)
- [Adding tests](#adding-tests)
- [Available Graphs](#available-graphs)

## Running the tests

Execute the following to download the dependencies and run the tests. Make sure you're in a venv.

```sh
echo '
HOST_NAME="https://tg-hostname"
USER_NAME=tigergraph
PASS=tigergraph
' >> test/.env
pip install -r requirements.txt
./run.sh
```

`test/.env`

- HOST_NAME: A TG environment that you have querywriter access to so setup.py can load data and queries to a subgraph named `graph_algorithms_testing`
- USER_NAME: user
- PASS: user's password

`run.sh` does a few things:

- runs `data/create_baseline.py`
  - this creates the baselines from the graphs listed in that file
- runs the setup script to make sure the graph is created and data is loaded
- runs the tests with pytest

## Directory layout

Data: stores the satic data for creating graphs, and algorithm baseline results.

- CSV files under `data/[heterogeneous_edges, unweighted_edges, weighted_edges]` store the adjacency information for creating graphs. The baselines for algorithms are made from these graphs
  - For example `data/weighted_edges/line_edges.csv` stores the edges and weights to create a weighted, line graph.
- JSON files under `data/baseline` store the baseline results for a given algorithm on a given graph type.
  - For example `data/baseline/centrality/pagerank/Line_Directed.json` stores the baseline results for pagerank on a directed line graph

test:

- setup.py: creates the graph, loads the data and installs the queries from pyTG's featurizer. Any new/custom queries need to be manually installed
- test<algo_family>.py: houses the testing code for each family of algorithms

```
├── data
│   ├── baseline
│   │   ├── <algo_family>
│   │   │   └── <algo_name>
│   │   │       └── <GraphType>.json
│   ├── <edge_family>
│   │   └── <graph_type>.csv
│   └── create_baseline.py
├── requirements.txt
├── run.sh
├── test
│   ├── pyrightconfig.json
│   ├── setup.py
│   ├── test_centrality.py
│   ├── test_community.py
│   ├── test_path_finding.py
│   ├── test_topological_link_prediction.py
│   └── util.py
```

## Adding tests

Start with creating the baseline. Add a section to `create_baseline.py` that creates a baseline for all the necessary graph types for your algorithm. The output of the baseline should be written to 
the correct baseline path (see above [layout](#directory-layout)).

If you're adding a new algorithm, add a test method for it to the algorithm family that it belongs to (i.e., community algorigthms go in community.py). The first test method in `test/test_centrality.py` 
is a good template to follow:

```py
    # this function will run once for each of the graph names in the undirected_graphs list
    @pytest.mark.parametrize("test_name", undirected_graphs)
    def test_degree_centrality1(self, test_name):
        # query params
        params = {
            "v_type_set": ["V20"],
            "e_type_set": [test_name],
            "reverse_e_type_set": [test_name],
            "in_degree": True,
            "out_degree": False,
            "top_k": 100,
            "print_results": True,
            "result_attribute": "",
            "file_path": "",
        }
        with open(f"data/baseline/centrality/degree_centrality/{test_name}.json") as f:
            baseline = json.load(f)
        baseline = sorted(baseline[0]["top_scores"], key=lambda x: x["Vertex_ID"])

        # call the the algorithm through the featurizer
        result = self.feat.runAlgorithm("tg_degree_cent", params=params)
        result = sorted(result[0]["top_scores"], key=lambda x: x["Vertex_ID"])


        # check that the results agree with the baseline
        for b in baseline:
            for r in result:
                if r["Vertex_ID"] == b["Vertex_ID"] and r["score"] != pytest.approx(
                    b["score"]
                ):
                    pytest.fail(f'{r["score"]} != {b["score"]}')
```

## Available Graphs

Example usage:

- If you want to run a query on a directed, weighted, line graph, use the V20 verts and Line_Directed_Weighted edges.

| Graph                       | Type                                                         | Vertices | Edges                            |
| --------------------------- | ------------------------------------------------------------ | -------- | -------------------------------- |
| Null                        |                                                              | V0       |                                  |
| Single node                 |                                                              | V1       |                                  |
| Empty graph                 | Undirected                                                   | V20      | Empty                            |
|                             | Directed                                                     |          | Empty_Directed                   |
| Line                        | Undirected, unweighted                                       | V20      | Line                             |
|                             | Directed, unweighted                                         |          | Line_Directed                    |
|                             | Undirected, weighted                                         |          | Line_Weighted                    |
|                             | Directed, weighted                                           |          | Line_Directed_Weighted           |
|                             | Heterogeneous vertex types, directed, weighted               | V20, V8  | Line_Heterogeneous               |
| Ring                        | Undirected, unweighted                                       | V20      | Ring                             |
|                             | Directed, unweighted                                         |          | Ring_Directed                    |
|                             | Undirected, weighted                                         |          | Ring_Weighted                    |
|                             | Directed, weighted                                           |          | Ring_Directed_Weighted           |
|                             | Heterogeneous vertex types, directed, weighted               | V20, V8  | Ring_Heterogeneous               |
| Hub & spoke                 | Undirected, unweighted                                       | V20      | Hub_Spoke                        |
|                             | Directed (towards the spokes), unweighted Hub_Spoke_Directed |          |                                  |
|                             | Undirected, weighted Hub_Spoke_Weighted                      |          |                                  |
|                             | Directed, weighted Hub_Spoke_Directed_Weighted               |          |                                  |
|                             | Heterogeneous vertex types, directed, weighted               | V20, V8  | Hub_Spoke_Heterogeneous          |
| Hub-connected hub & spoke   | Undirected, unweighted                                       | V20      | Hub_Connected_Hub_Spoke          |
|                             | Undirected, weighted                                         |          | Hub_Connected_Hub_Spoke_Weighted |
| Tree                        | Undirected, unweighted                                       | V20      | Tree                             |
|                             | Directed, unweighted                                         |          | Tree_Directed                    |
|                             | Undirected, weighted                                         |          | Tree_Weighted                    |
|                             | Directed, weighted                                           |          | Tree_Directed_Weighted           |
|                             | Heterogeneous vertex types, directed, weighted               | V20, V8  | Tree_Heterogeneous               |
| Complete                    | Undirected, unweighted                                       | V8       | Complete                         |
|                             | Directed, unweighted                                         |          | Complete_Directed                |
|                             | Undirected, weighted                                         |          | Complete_Weighted                |
|                             | Directed, weighted                                           |          | Complete_Directed_Weighted       |
|                             | Heterogeneous vertex types, directed, weighted               | V4, V8   | Complete_Heterogeneous           |
| DAG                         | Directed, unweighted                                         | V20      | DAG_Directed                     |
|                             | Directed, weighted                                           |          | DAG_Directed_Weighted            |
|                             | Heterogeneous vertex types, directed, weighted               | V20, V8  | DAG_Heterogeneous                |
| Graph with negative cycles  | Directed, weighted                                           | V20      | Negative_cycles                  |
|                             | Heterogeneous vertex types, directed, weighted               | V20, V8  | Negative_Cycle_Heterogeneous     |
| Topological link prediction | Unweighted, undirected                                       | V8       | topo_link1                       |
|                             | topo_link2                                                   |          |                                  |
|                             | topo_link3                                                   |          |                                  |
|                             | topo_link4                                                   |          |                                  |
|                             | topo_link5                                                   |          |                                  |
|                             | topo_link6                                                   |          |                                  |
|                             | Unweighted, directed                                         |          | topo_link_directed               |
| Same Community              | no edges                                                     | V4       |                                  |
