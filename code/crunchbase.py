import networkx as nx

import requests
import simplejson as json

from collections import deque

base_url = 'http://api.crunchbase.com/v/1/company/'
ext = '.js'

def get_data(seed='facebook'):
    companies = nx.Graph()
    queue = deque()
    visited = []
    if hasattr(seed, '__iter__'):
        queue.extend(seed)
    else:
        queue.append(seed)

    while len(queue)>0:
        company = queue.popleft()
        url = base_url + company + ext
        visited.append(company)

        print company, url
        resp = requests.get(url)
        data = json.loads(resp.content)

        for c in data['competitions']:
            companies.add_edge(company,c['competitor']['name'])
            if c['competitor']['name'] not in visited:
                queue.append(c['competitor']['permalink'])
    return companies

