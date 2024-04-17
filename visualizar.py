import community as community_louvain
from matplotlib import pyplot as plt
from matplotlib import cm as cm
import networkx as nx

def visualize_network():
    arquivo = './txts/conexoes.txt'

    # Constrói o grafo
    G = nx.Graph()
    
    with open(arquivo, 'r') as f:
        for linha in f:
            novaLinha = linha.strip()
            num1 = int(novaLinha.split(' ')[0])
            num2 = int(novaLinha.split(' ')[1])
            num3 = int(novaLinha.split(' ')[2])
            G.add_weighted_edges_from([(num1, num2, num3)])

    # Aplica o algoritmo de detecção de comunidades Louvain
    partition = community_louvain.best_partition(G)

    # Posiciona os nós usando o algoritmo de layout spring
    pos = nx.spring_layout(G)

    # Define o mapa de cores com base no número de comunidades
    cmap = plt.get_cmap('viridis', max(partition.values()) + 1)

    # Desenha os nós com cores diferentes com base em sua pertinência à comunidade
    nx.draw_networkx_nodes(G, pos, partition.keys(), cmap=cmap, node_color=list(partition.values()))

    # Desenha as arestas
    nx.draw_networkx_edges(G, pos, alpha=0.5)

    # Desenha as etiquetas dos nós
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')

    # Exibe a visualização da rede
    plt.show()

if __name__ == '__main__':
    visualize_network()
