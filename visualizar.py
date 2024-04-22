import community as community_louvain
from matplotlib import pyplot as plt
from matplotlib import cm as cm
import networkx as nx

def get_list_list(particionamento):
    lista_de_listas = []
    comunidades = set(particionamento.values())

    for comunidade in comunidades:
        indices_comunidade = [indice for indice, classe in particionamento.items() if classe == comunidade]
        lista_de_listas.append(indices_comunidade)
    
    return lista_de_listas

def printComunidades(l1, arq):
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
    # with open('./gabriel/comunidades.txt', "w") as f:
    with open('./vinicius/comunidades_vinicius.txt', "w") as f:
        for pessoas in l1:
            f.write(f"Comunidade {i}: \n")
            for pessoa in pessoas:
                f.write(pessoasArquivo[str(pessoa)] + "\n")
            i += 1

def visualize_network():
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

    pos = nx.spring_layout(G)
    partitions = community_louvain.best_partition(G)
    comunidades = set(partitions.values())
    num_comunidades = len(comunidades)
    print('Número de comunidades:', num_comunidades)
    cores = ['blue', 'green', 'yellow', 'purple', 'orange']
    nx.draw_networkx_nodes(G, pos, node_size=50, node_color=[cores[partitions[node]] for node in G.nodes()], alpha=0.5)
    nx.draw_networkx_edges(G, pos, alpha=0.1)
    nx.draw_networkx_labels(G, pos, font_size=6, font_color='black')
    plt.show()
    
    comunidade_ego = get_list_list(partitions)
    # printComunidades(comunidade_ego, './gabriel/pessoas.txt')
    printComunidades(comunidade_ego, './vinicius/pessoas_vinicius.txt')

if __name__ == '__main__':
    visualize_network()
