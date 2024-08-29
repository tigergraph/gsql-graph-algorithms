import networkx as nx


def create_graph(edges, weights=False, directed=False) -> nx.Graph:
    if directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    if weights:
        # make weights floats
        edges = [[a, b, float(c)] for a, b, c in edges]
        g.add_weighted_edges_from(edges)
    else:
        g.add_edges_from(edges)
    return g
