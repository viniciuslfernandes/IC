import networkx as nx
import igraph as ig
from matplotlib import pyplot as plt

if __name__ == '__main__':
    arquivo = './txts/conexoes.txt'
    arquivo2 = './txts/pessoas.txt'

    # utilizando a biblioteca networkx para visualizar o grafo
    # G = nx.DiGraph()
    
    # with open(arquivo, 'r') as f:
    #     for linha in f:
    #         novaLinha = linha.strip()
    #         num1 = novaLinha.split(' ')[0]
    #         num2 = novaLinha.split(' ')[1]
    #         num3 = novaLinha.split(' ')[2]
    #         G.add_weighted_edges_from([(num1, num2, num3)])

    # print(G.number_of_edges())
    # print(G.number_of_nodes())
    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()

    # utilizando a biblioteca igraph para visualizar o grafo
    # G = ig.Graph()

    # with open(arquivo2, 'r') as f:
    #     linhas = f.readlines()
    #     vertices = len(linhas)
    #     G.add_vertices(vertices)

    # with open(arquivo, 'r') as f:
    #     arestas = []
    #     pesos = []
    #     for linha in f:
    #         novaLinha = linha.strip()
    #         num1 = int(novaLinha.split(' ')[0])
    #         num2 = int(novaLinha.split(' ')[1])
    #         num3 = int(novaLinha.split(' ')[2])
    #         arestas.append((num1, num2))
    #         pesos.append(num3)

    # G.add_edges(arestas)
    # layout = G.layout("kk")
    # fig, ax = plt.subplots()
    # ig.plot(G, layout=layout, target=ax)
    
    # utilizando a biblioteca gephi para visualizar o grafo
    