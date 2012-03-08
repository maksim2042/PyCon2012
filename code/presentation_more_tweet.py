# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import collection
#reload collection

# <codecell>

collection.rsearch('pycon')
# What is happening here?
# r = requests.post('http://search.twitter.com/search.json', data={'q':'#pycon'})

# <codecell>

# redefine 
collection.process_tweet = collection.process_retweets

# <codecell>

collection.rsearch('pycon')

# <codecell>


