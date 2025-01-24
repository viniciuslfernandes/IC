from matplotlib import pyplot as plt
from operator import itemgetter
import cdlib
import matplotlib
import ndlib.models.CompositeModel as gc
import ndlib.models.compartments as cpm
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc
import networkx as nx
import random
import csv
import pandas as pd
matplotlib.use('TkAgg')

RESULTADO_ESPERADO_GABRIEL = [
                                [2, 4, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 293, 294, 295, 296, 299], 
                                [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 304], 
                                [1, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 280, 281, 284, 285, 286, 287, 289, 290, 297, 298, 301, 302, 303, 305, 306, 307, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377], 
                                [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206], 
                                [207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 282, 283, 288, 291, 292, 300, 308, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394]
                            ]

RESULTADO_ESPERADO_VINICIUS = [
                                [1, 346, 347, 348, 349, 350, 351, 352, 353, 354, 357, 359, 360, 361, 362, 452, 480, 148, 149, 340, 341, 342, 356, 355, 358, 277, 339, 382, 433, 445, 150, 274, 275, 276, 312, 313, 314, 315, 316, 328, 330, 335, 336, 363, 366, 365, 364, 383, 384, 420, 419, 427, 428, 429, 435, 436, 37, 438, 444, 443, 441, 440, 439, 446, 456, 453, 457, 458, 459, 460, 474, 479, 481, 497, 498, 511, 478, 477, 447, 448, 449, 450, 451, 136, 137, 145, 144, 142, 141 , 140, 139, 138, 434, 332, 292, 367, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 381, 368, 380, 190, 191, 240, 281, 285, 475, 476, 524, 232, 278, 513, 508],
                                [7, 393, 394, 397, 399, 403, 404, 405, 400, 402, 416, 392, 396, 408, 410, 413, 415, 414, 412, 417, 423, 503, 272, 338, 395, 398, 401, 406, 407, 409, 411, 418, 422, 421, 489, 495, 496, 391, 298, 462, 470, 469, 468, 467, 466, 465, 463, 464],
                                [40, 41, 42, 44, 494, 499, 43, 47, 48, 49, 50, 51, 54, 88, 100, 102, 108, 112, 118, 193, 194, 264, 287, 389, 55, 56, 57, 75, 91, 110, 134, 135, 189, 192, 247, 248, 260, 280, 286, 293, 304, 308, 343, 390, 432, 519, 537, 105, 107, 117, 52, 53, 73, 89, 90, 93, 94, 99, 98, 96, 97, 95, 101, 103, 104, 106, 109, 116, 119, 120, 125, 195, 197, 256, 261, 273, 282, 283, 289, 299, 300, 301, 302, 303, 305, 306, 307, 309, 310, 311, 319, 320, 321, 322, 324, 325, 326, 327, 329, 333, 337, 424, 426, 430, 431, 455, 454, 461, 482, 483, 490, 491, 512, 514, 515, 516, 522, 525, 526, 527, 528, 530, 534, 536, 425, 538, 45, 500, 269, 296],
                                [3, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 17, 203, 204, 209, 210, 233, 268, 86, 127, 129, 132, 178, 208, 252, 253, 254, 255, 152, 153, 154, 235, 238, 239, 257, 270, 344, 345, 385, 386, 387, 388, 471, 473, 16, 62, 61, 65, 68, 69, 70, 74, 77, 121, 211, 212, 215, 216, 218, 219, 220, 226, 228, 237, 236, 295, 318, 485, 486, 505, 472, 229, 67, 501, 63, 66, 71, 72, 78, 79, 81, 80, 82, 83, 84, 85, 87, 92, 113, 114, 115, 128, 130, 147, 146, 155, 199, 200, 201, 205, 207, 206, 213, 214, 217, 221, 223, 224, 225, 227, 230, 231, 234, 241, 249, 258, 267, 271, 279, 317, 334, 484, 487, 488, 493, 504, 506, 507, 529, 532, 76, 222, 250, 442, 124],
                                [19, 21, 22, 23, 24, 18, 20, 26, 39, 59, 64, 133, 184, 46, 58, 111, 131, 179, 185, 187, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 171, 172, 173, 174, 175, 176, 177, 180, 182, 181, 183, 331, 14, 27, 28, 25, 29, 30, 32, 33, 34, 36, 262, 263, 266, 284, 323, 518, 521, 531, 122, 502, 31, 35, 37, 38, 60, 123, 126, 151, 169, 170, 186, 188, 196, 198, 202, 242, 243, 244, 245, 246, 251, 259, 265, 288, 290, 291, 294, 297, 492, 509, 510, 517, 520, 523, 533, 535, 143]
                            ]

def criar_lista_de_listas(particionamento):
    lista_de_listas = []
    comunidades = set(particionamento.values())

    for comunidade in comunidades:
        indices_comunidade = [indice for indice, classe in particionamento.items() if classe == comunidade]
        lista_de_listas.append(indices_comunidade)
    
    return lista_de_listas

def escrever_comunidades(l1, arq, arq2, opcao_arquivo):
    pessoasArquivo = {}
    with open(arq, "r") as f:
        next(f)
        for line in f:
            if opcao_arquivo == '1':
                fields = line.strip().split(',')
            elif opcao_arquivo == '2':
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
            f.write("\n")

def similaridade_comunidades(l1, l2):
    totalElementos = 0
    similaridade = 0
    for lista1 in l1:
        taml1 = len(lista1)
        totalElementos += taml1

        setl1 = set(lista1)
        maiorSemelhanca = 0
        for lista2 in l2:
            setl2 = set(lista2)
            common = setl1.intersection(setl2)
            if len(common) > maiorSemelhanca:
                maiorSemelhanca = len(common)

        similaridade += maiorSemelhanca

    print(f"Similaridade: {similaridade/totalElementos}")

def criar_grafo(opcao_arquivo):
    if opcao_arquivo == '1':
        arquivo = './gabriel/conexoes.txt'
    elif opcao_arquivo == '2':
        arquivo = './vinicius/conexoes_vinicius.txt'
    elif opcao_arquivo == '3':
        arquivo = './generico_seir.txt'
    else:
        print("Opção de arquivo inválida")
        exit()

    G = nx.Graph()
    
    with open(arquivo, 'r') as f:
        for linha in f:
            novaLinha = linha.strip()
            num1 = int(novaLinha.split(' ')[0])
            num2 = int(novaLinha.split(' ')[1])
            num3 = int(novaLinha.split(' ')[2])
            G.add_weighted_edges_from([(num1, num2, num3)])

    return G

def visualizar_grafo_louvain(G, opcao_arquivo):
    coms = cdlib.algorithms.louvain(G)
    pos = nx.spring_layout(G)
    cdlib.viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego_louvain = criar_lista_de_listas(partitions)
    
    if opcao_arquivo == '1':
        similaridade_comunidades(RESULTADO_ESPERADO_GABRIEL, comunidade_ego_louvain)
        escrever_comunidades(comunidade_ego_louvain, './gabriel/pessoas.txt', './gabriel/comunidades/louvain.txt', opcao_arquivo)
    elif opcao_arquivo == '2':
        similaridade_comunidades(RESULTADO_ESPERADO_VINICIUS, comunidade_ego_louvain)
        escrever_comunidades(comunidade_ego_louvain, './vinicius/pessoas_vinicius.txt', './vinicius/comunidades/louvain.txt', opcao_arquivo)

def visualizar_grafo_leiden(G, opcao_arquivo):
    coms = cdlib.algorithms.leiden(G)
    pos = nx.spring_layout(G)
    cdlib.viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego_leiden = criar_lista_de_listas(partitions)

    if opcao_arquivo == '1':
        similaridade_comunidades(RESULTADO_ESPERADO_GABRIEL, comunidade_ego_leiden)
        escrever_comunidades(comunidade_ego_leiden, './gabriel/pessoas.txt', './gabriel/comunidades/leiden.txt', opcao_arquivo)
    elif opcao_arquivo == '2':
        similaridade_comunidades(RESULTADO_ESPERADO_VINICIUS, comunidade_ego_leiden)
        escrever_comunidades(comunidade_ego_leiden, './vinicius/pessoas_vinicius.txt', './vinicius/comunidades/leiden.txt', opcao_arquivo)

def visualizar_grafo_rb_pots(G, opcao_arquivo):
    coms = cdlib.algorithms.rb_pots(G)
    pos = nx.spring_layout(G)
    cdlib.viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego_rb_pots = criar_lista_de_listas(partitions)

    if opcao_arquivo == '1':
        similaridade_comunidades(RESULTADO_ESPERADO_GABRIEL, comunidade_ego_rb_pots)
        escrever_comunidades(comunidade_ego_rb_pots, './gabriel/pessoas.txt', './gabriel/comunidades/rb_pots.txt', opcao_arquivo)
    elif opcao_arquivo == '2':
        similaridade_comunidades(RESULTADO_ESPERADO_VINICIUS, comunidade_ego_rb_pots)
        escrever_comunidades(comunidade_ego_rb_pots, './vinicius/pessoas_vinicius.txt', './vinicius/comunidades/rb_pots.txt', opcao_arquivo)

def visualizar_grafo_surprise_communities(G, opcao_arquivo):
    coms = cdlib.algorithms.surprise_communities(G)
    pos = nx.spring_layout(G)
    cdlib.viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego_surprise_communities = criar_lista_de_listas(partitions)

    if opcao_arquivo == '1':
        similaridade_comunidades(RESULTADO_ESPERADO_GABRIEL, comunidade_ego_surprise_communities)
        escrever_comunidades(comunidade_ego_surprise_communities, './gabriel/pessoas.txt', './gabriel/comunidades/surprise_communities.txt', opcao_arquivo)
    elif opcao_arquivo == '2':
        similaridade_comunidades(RESULTADO_ESPERADO_VINICIUS, comunidade_ego_surprise_communities)
        escrever_comunidades(comunidade_ego_surprise_communities, './vinicius/pessoas_vinicius.txt', './vinicius/comunidades/surprise_communities.txt', opcao_arquivo)

def visualizar_grafo_threshold_clustering(G, opcao_arquivo):
    coms = cdlib.algorithms.threshold_clustering(G)
    pos = nx.spring_layout(G)
    cdlib.viz.plot_network_clusters(G, coms, pos, node_size=50)
    plt.show()

    partitions = dict([])
    for cid, community in enumerate(coms.communities):
        for node in community:
            partitions[node] = cid
            
    comunidade_ego_threshold_clustering = criar_lista_de_listas(partitions)

    if opcao_arquivo == '1':
        similaridade_comunidades(RESULTADO_ESPERADO_GABRIEL, comunidade_ego_threshold_clustering)
        escrever_comunidades(comunidade_ego_threshold_clustering, './gabriel/pessoas.txt', './gabriel/comunidades/threshold_clustering.txt', opcao_arquivo)
    elif opcao_arquivo == '2':
        similaridade_comunidades(RESULTADO_ESPERADO_VINICIUS, comunidade_ego_threshold_clustering)
        escrever_comunidades(comunidade_ego_threshold_clustering, './vinicius/pessoas_vinicius.txt', './vinicius/comunidades/threshold_clustering.txt', opcao_arquivo)

def visualizar_grafo(G):
    # find node with largest degree
    node_and_degree = G.degree()
    (largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]

    # Create ego graph of main hub
    hub_ego = nx.ego_graph(G, largest_hub)

    # Draw graph
    pos = nx.spring_layout(hub_ego, seed=20532)  # Seed layout for reproducibility
    nx.draw(hub_ego, pos, node_color="b", node_size=50, with_labels=False, width=0.1, edge_color="grey")

    # Draw ego as large and red
    options = {"node_size": 150, "node_color": "g"}
    nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], **options)
    plt.show()

if __name__ == '__main__':
    opcao_arquivo = input("Digite 1 para visualizar o grafo de Gabriel ou 2 para visualizar o grafo de Vinicius ou 3 para um grafo Generico: \n")
    grafo = criar_grafo(opcao_arquivo)
    
    # valores = [(0.35/7, 0.567/7)]
    valores = [(0.370057653, 0.1)]
    
    ego = [1]
    forte = []
    ponte = []
    fraco = []
    
    for (v1, v2 ) in grafo.edges(0):
        peso = grafo.get_edge_data(v1, v2)['weight']
        # print(f'aresta: {v1, v2} | peso: {peso}')
        if peso == 1:
            forte.append(v2)
        elif peso == 2:
            ponte.append(v2)
        elif peso == 3:
            fraco.append(v2)
            
    classes_iniciais = [forte, ponte, fraco]
    
    column = ['0', '5', '10', '15', '20', '25', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '179']
    # with open('./tabelas_seir/teste.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    #     columns = csv.DictWriter(csvfile, fieldnames=column)
    #     columns.writeheader()
    
    for i in range(len(valores)):
        classes_tamanho = []
        
        for a in classes_iniciais:
            classes_tamanho.append(len(a))
            
        for c in range(1):
            iteracao_infectado = []
            classes_infectado = [[], [], []]         
            porcentagem_infectados= [[], [], []]
            # for k in ego:
            for k in forte:
            # for k in ponte:
            # for k in fraco:
                
                print(f"SIMULAÇÃO no: {k} ")
                classes = [lista[:] for lista in classes_iniciais]
                # grafo_aux = []
                # for z in range(len(grafo)):
                #     grafo_aux.append(z)
                
                # Model Selection
                model = ep.SEIRModel(grafo)

                # Model Configuration
                config = mc.Configuration()
                config.add_model_parameter("beta", valores[i][0])
                config.add_model_parameter("gamma", valores[i][1])
                config.add_model_parameter('alpha', 0.05)
                # config.add_model_parameter("fraction_infected", 0.05)
                # config.add_model_parameter("fraction_infected", 0.01)
                
                
                # if(k>=15):
                #     no_maior_grau = grau_medio
                config.add_model_initial_configuration("Infected", [k])

                for (u, v, data) in grafo.edges(data=True):
                    weight = data['weight']
                    config.add_edge_configuration((u, v), 'threshold',  valores[i][0] * (4 - weight ) / 3)
                # Simulation execution
                model.set_initial_status(config)
                num_iteracoes =180
                
                iterations = model.iteration_bunch(num_iteracoes)
                suscetiveis = []
                infectados = []
                recuperados = []
                
                # valores_iter = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 179]
                dados =[]
                    
                # for a in classes:
                #     if k in a:
                #         a.remove(k)
                
                # status: 0 - suscetível || 1 - infectado || 2 - Exposto || 3- recuperado
                for j in iterations:
                    # suscetiveis.append(j['node_count'][0])
                    # infectados.append(j['node_count'][1])
                    # recuperados.append(j['node_count'][2])
                    for x in j['status']:
                    # if x == 1 and j['status'][x]==1:
                    #     iteracao_infectado.append(j['iteration'])
                        if j['status'][x]==1:
                                # if x in grafo_aux:
                                #     grafo_aux.remove(x)
                                if x in classes[0]:
                                    classes[0].remove(x)
                                    if(len(classes[0])==0):
                                        classes_infectado[0].append(j['iteration'])
                                
                                elif x in classes[1]:
                                    classes[1].remove(x)
                                    if(len(classes[1])==0):
                                        classes_infectado[1].append(j['iteration'])
                                        
                                elif x in classes[2]:
                                    classes[2].remove(x)
                                    if(len(classes[2])==0):
                                        classes_infectado[2].append(j['iteration'])

                            
                pos = 0
                for a in classes:
                    if(classes_tamanho[pos]!=0):
                        porcentagem = ((classes_tamanho[pos]- len(a))*100)/classes_tamanho[pos]
                        porcentagem_infectados[pos].append(porcentagem)
                    pos+=1       
                    # print(f"quantidade de pessoas no grafo: {len(grafo)}")
                    # print(f"quantidade de pessoas no grafo aux: {len(grafo_aux)}")
                    # print(f"iteracao: {j['iteration']}  e  status: {j['status']}") 
                    # print(f"a porcentagem de infectados na iteracao {k}: {((len(grafo)) - len(grafo_aux))*100 / len(grafo)}\n")
                

                # row = {str(column[i]): dados[i] for i in range(len(column))}
                # columns.writerow(row)
            
            porcentagem_forte = sum(porcentagem_infectados[0])/len(porcentagem_infectados[0])
            # # print(f'porcentagem ponte: {sum(porcentagem_infectados[1])/len(porcentagem_infectados[1])}')
            porcentagem_ponte = sum(porcentagem_infectados[1])/len(porcentagem_infectados[1])
            # print(f'porcentagem fraco: {sum(porcentagem_infectados[2])/len(porcentagem_infectados[2])}')
            porcentagem_fraco = sum(porcentagem_infectados[2])/len(porcentagem_infectados[2])
            with open('./tabelas_seir/tabela_porcentagem_classes.csv', 'a') as f:
                f.write(f'{porcentagem_forte} {porcentagem_ponte} {porcentagem_fraco}\n')
                
            print(classes_infectado)
            if(len(classes_infectado[0])==0):
                classes_infectado[0].append(0)
                
            if(len(classes_infectado[1])==0):
                classes_infectado[1].append(0)
                
            if(len(classes_infectado[2])==0):
                classes_infectado[2].append(0)
            tempo_forte =  sum(classes_infectado[0])/len(classes_infectado[0])
            # print(f"media ponte: {sum(classes_infectado[1])/len(classes_infectado[1])}")
            tempo_ponte =  sum(classes_infectado[1])/len(classes_infectado[1])
            # print(f"media fraco: {sum(classes_infectado[2])/len(classes_infectado[2])}")
            tempo_fraco=  sum(classes_infectado[2])/len(classes_infectado[2])
            with open('./tabelas_seir/tabela_tempo_classes.csv', 'a') as f:
                f.write(f'{tempo_forte} {tempo_ponte} {tempo_fraco}\n')
    # tabela = pd.read_csv('generico_no_medio.csv.csv')
    # print(tabela)