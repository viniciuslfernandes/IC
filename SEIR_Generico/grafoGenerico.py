import random
import networkx as nx

grafo = nx.Graph()
range_grafo = range(1, 51147)
grafo.add_nodes_from(range_grafo)
for i in range_grafo:
    for j in range(i, len(range_grafo)):
        if(random.random() >= 0.91): #0,9% da população de 51145 pessoas, = aproximadamente 460 pessoas
            if i!=j:
                grafo.add_weighted_edges_from([(i, j, 1)])

arestas_append = set()

with open('./generico_seir.txt', 'w') as f:
    for u, v, weight in grafo.edges(data=True):
        if (u, v) not in arestas_append and (v, u) not in arestas_append:
            f.write(f"{u} {v} {weight['weight']}\n")
            f.write(f"{v} {u} {weight['weight']}\n")
            arestas_append.add((u, v))
            arestas_append.add((v, u))