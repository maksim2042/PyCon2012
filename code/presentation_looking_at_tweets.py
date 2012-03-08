# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import gzip
f = gzip.open('data.json.gz')

# <codecell>

# View the first line of the json
f.readline()

# <codecell>

tweets = list(gzip.open('data.json.gz'))

# <codecell>

len(tweets)

# <codecell>

# out last tweet is bad, so let's delete it
# tweets[-1]
del tweets[-1]

# <codecell>

# right now they are just strings, so let's make them serialable objects
import simplejson
tweets = map(simplejson.loads, tweets)
# We use simplejson, because it is faster than the built in json

# <codecell>

# Grab screenname of first user
tweets[0]['user']['screen_name']
# The result is going to be the from

# <codecell>

tweets[0]['entities']['user_mentions']
# So there will be an edge between joshbarone & the dailybeast

# <codecell>

import collection

# <codecell>

# let's create a retweet map
retweets = map(collection.process_retweets, tweets)
# if you want to redo this, you need to reimport collections to reinitial the graph.
# Then rerun the process_retweets

# <codecell>

type(retweets)

# <codecell>

import networkx as nx

# <codecell>

deg = nx.degree(retweets)

# <codecell>

max(deg.values())

# <codecell>

# trim out all the nodes with a degree of 1
g2 = util.trim_degrees(g)

# <codecell>

# how many do we have left?
len(g2)
# 7900, so that is quite a bit still, let's trim more

# <codecell>

g2 = util.trim_degrees(g2)
g2 = util.trim_degrees(g2)
g2 = util.trim_degrees(g2)
# continue to run it until len(g2) stops changes

# <codecell>

# To compute closeness - we are going to skip this, because it TAKES FOREVER!
# So we are going to do page rank
pr = nx.pagerank(g2)
plot.hist(pr.values, 100)

# <codecell>

import util

# <codecell>

sd = util.sorted_degree(g)

# <codecell>

g.remove_edges_from(g.selfloop_edges())
core = nx.k_core(g, k=1)
len(core)
core = nx.k_core(g, k=2)
core = nx.k_core(g, k=3)
len(core)
# 167

