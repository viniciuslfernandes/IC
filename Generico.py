import random
import networkx as nx

grafo = nx.Graph()
range_grafo = range(0, 1000)
grafo.add_nodes_from(range_grafo)
for i in range_grafo:
    for j in range(i, len(range_grafo)):
        if(random.random() >= 0.97):
            if i!=j:
                grafo.add_weighted_edges_from([(i, j, 1)])
        elif(random.random() >= 0.95):
            if i!=j:
                grafo.add_weighted_edges_from([(i, j, 2)])
        elif(random.random() >= 0.9):
            if i!=j:
                grafo.add_weighted_edges_from([(i, j, 3)])

with open('generico_seir.txt', 'w') as f:
    for u, v, weight in grafo.edges(data=True):
        f.write(f"{u} {v} {weight['weight']}\n")
        f.write(f"{v} {u} {weight['weight']}\n")