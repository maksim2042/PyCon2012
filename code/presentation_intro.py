# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import networkx as nx

# <codecell>

# Create a graph
g = nx.Graph()

# <codecell>

# Add some nodes
g.add_node(1)
g.add_node(2)
g.add_nodes_from("asdf")

# <codecell>

# Show the nodes
g.nodes()

# <codecell>

list(g.nodes_iter())

# <codecell>

# Get information on nodes
g.nodes?

# <codecell>

# draw the network
nx.draw(g)

# <codecell>

# add some edges
g.add_edge(1,2)
g.add_edge(1,'foo')
nx.draw(g)

# <codecell>

# Everything in networkx is a dict, so you can treat everything that way
g.__dict__

# <codecell>

g.node[1]
# Is an empty dict, so let's add something

# <codecell>

g.node[1]['foobar'] = 1
g.node[2]['foobar'] = 3

# <codecell>

# add weight

# <codecell>

# undirect graph
nx.Graph()
# directed graph
nx.DiGraph()

# <codecell>

g = nx.small.krackhardt_kite_graph()

# <codecell>

g.node

# <codecell>

g.nodes()

# <codecell>

# agency list
g.edges()

# <codecell>

nx.draw(g)

# <codecell>

d = nx.to_dict_of_dicts(g)
# same as 
# nx.edges

# <codecell>

# Create a new graph from our dict_of_dicts
g2 = nx.from_dict_of_dicts(d)

# <codecell>

# dumps as a json object
import simplejson
simplejson.dumps(nx.to_dict_of_dicts(g))

# <codecell>

import pickle
s = pickle.dumps(g)
g3 = pickle.loads(s)
nx.draw(g3)

# <codecell>

# Write out to pajek to interchange data with other files
nx.write_pajek(g, 'foo.net')
!cat foo.net

# <codecell>


# <codecell>


