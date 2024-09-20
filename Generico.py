import random
import networkx as nx

grafo = nx.Graph()
range_grafo = range(0, 100)
grafo.add_nodes_from(range_grafo)
for i in range_grafo:
    for j in range(i, len(range_grafo)):
        if(random.random() >= 0.9):
            if i!=j:
                grafo.add_weighted_edges_from([(i, j, 1)])

with open('generico.txt', 'w') as f:
    for u, v, weight in grafo.edges(data=True):
        f.write(f"{u} {v} {weight['weight']}\n")