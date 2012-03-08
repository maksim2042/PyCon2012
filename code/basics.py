import networkx as nx

g1 = nx.small.krackhardt_kite_graph()

# harder to serialize
from datetime import datetime
g2 = nx.Graph(g1)
g2.add_edge(1, datetime.now())
