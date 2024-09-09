# Algorithm Testing

[networkX](https://networkx.org/documentation/stable/reference/index.html) is used as
the baseline for our tests where we can.

A peculiarity to note about nx is that it counts self edges in undirected graphs as two separate edges. So, you'll see that some baselines use a modified version of the code that is found within nx. Take `run_degree_baseline_complete`, which generates the baseline for degree centrality on complete graphs. It uses the same code that can be found in `nx.centrality.degree_centrality` with the exception of subtracting a node's degree by one.
