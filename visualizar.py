from cdlib import algorithms, viz
from matplotlib import pyplot as plt
import networkx as nx

def get_list_list(particionamento):
    lista_de_listas = []
    comunidades = set(particionamento.values())

    for comunidade in comunidades:
        indices_comunidade = [indice for indice, classe in particionamento.items() if classe == comunidade]
        lista_de_listas.append(indices_comunidade)
    
    return lista_de_listas

def printComunidades(l1, arq, arq2):
    pessoasArquivo = {}
    with open(arq, "r") as f:
        next(f)
        for line in f:
            # fields = line.strip().split(',')
            fields = line.strip().split('\t')
            if len(fields) >= 4:
                nome, apelido, cidade = fields[1], fields[2], fields[3]
                pessoasArquivo[fields[0]] = f"{fields[0]} - {nome}, {apelido}, {cidade}"

    i = 1
    with open(arq2, "w") as f:
        for pessoas in l1:
            f.write(f"Comunidade {i}: \n")
            for pessoa in pessoas:
                f.write(pessoasArquivo[str(pessoa)] + "\n")
            i += 1

def visualizar_grafo_louvain(G):
    coms = algorithms.louvain(G)

    # plota as comunidades em si
    # viz.plot_community_graph(G, coms)

    # plota o grafo completo
    pos = nx.spring_layout(G)
    viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego = get_list_list(partitions)
    # printComunidades(comunidade_ego, './gabriel/pessoas.txt', './gabriel/louvain.txt')
    printComunidades(comunidade_ego, './vinicius/pessoas_vinicius.txt', './vinicius/louvain.txt')

def visualizar_grafo_leiden(G):
    coms = algorithms.leiden(G)

    # plota as comunidades em si
    # viz.plot_community_graph(G, coms)

    # plota o grafo completo
    pos = nx.spring_layout(G)
    viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego = get_list_list(partitions)
    # printComunidades(comunidade_ego, './gabriel/pessoas.txt', './gabriel/leiden.txt')
    printComunidades(comunidade_ego, './vinicius/pessoas_vinicius.txt', './vinicius/leiden.txt')

def criar_grafo():
    # arquivo = './gabriel/conexoes.txt'
    arquivo = './vinicius/conexoes_vinicius.txt'

    G = nx.Graph()
    
    with open(arquivo, 'r') as f:
        for linha in f:
            novaLinha = linha.strip()
            num1 = int(novaLinha.split(' ')[0])
            num2 = int(novaLinha.split(' ')[1])
            num3 = int(novaLinha.split(' ')[2])
            G.add_weighted_edges_from([(num1, num2, num3)])

    return G

if __name__ == '__main__':
    grafo = criar_grafo()
    visualizar_grafo_louvain(grafo)
    visualizar_grafo_leiden(grafo)