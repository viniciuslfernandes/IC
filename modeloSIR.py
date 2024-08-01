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
    opcao_arquivo = input("Digite 1 para visualizar o grafo de Gabriel ou 2 para visualizar o grafo de Vinicius: \n")
    grafo = criar_grafo(opcao_arquivo)

    # grafo = nx.Graph()
    # range_grafo = range(0, 1000)
    # grafo.add_nodes_from(range_grafo)
    # for i in range_grafo:
    #     for j in range(i, len(range_grafo)):
    #         if(random.random() >= 0.9):
    #             grafo.add_weighted_edges_from([(i, j, 1)])

    # (beta, gamma)
    # valores = [(0.00000000035266, 1/15), (0.1875, 0.0508), (0.3077, 1/5.2), (0.17, 0.7142), (0.216, 0.102), (0.126, 0.083), (0.34, 0.119), (0.34, 0.182)]
    # valores = [(0.0026, 0.0012), (0.35/7, 0.567/7), (0.5/5, 0.07), (0.5/50, 0.07), (0.5/100, 0.07), (0.202, 1/14)]
    valores = [(0.35/7, 0.567/7)]
    
    familia = []
    melhor_amigo = []
    namorado = []
    amigo = []
    parente = []
    parca = []
    professor = []
    aluno = []
    colega = []
    trabalho = []
    consanguineo = []
    ficante = []
    conhecido = []

    for (v1, v2 ) in grafo.edges(1):
        peso = grafo.get_edge_data(v1, v2)['weight']
        # print(f'aresta: {v1, v2} | peso: {peso}')
        if peso == 1:
            familia.append(v2)
        elif peso == 2:
            melhor_amigo.append(v2)
        elif peso == 3:
            namorado.append(v2)
        elif peso == 4:
            amigo.append(v2)
        elif peso == 5:
            parente.append(v2)
        elif peso == 6:
            parca.append(v2)
        elif peso == 7:
            aluno.append(v2)
        elif peso == 8:
            professor.append(v2)
        elif peso == 9:
            colega.append(v2)
        elif peso == 10:
            trabalho.append(v2)
        elif peso == 11:
            consanguineo.append(v2)
        elif peso == 12:
            ficante.append(v2)
        elif peso == 13:
            conhecido.append(v2)

    classes_iniciais = [familia, melhor_amigo, namorado, amigo, parente, parca, professor, aluno, colega, trabalho, consanguineo, ficante, conhecido]
    
    for i in range(len(valores)):
        iteracao_infectado = []
        classes_infectado = [[], [], [], [], [], [], [], [], [], [], [], [], []]
        porcentagem_infectados= [[], [], [], [], [], [], [], [], [], [], [], [], []]
        classes_tamanho = []
        
        for a in classes_iniciais:
            classes_tamanho.append(len(a))
        
        # for k in familia:
        # for k in melhor_amigo:
        # for k in namorado:
        # for k in amigo:
        # for k in parente:
        # for k in parca:
        # for k in professor:
        # for k in aluno:
        # for k in colega:
        # for k in trabalho:
        # for k in consanguineo:
        # for k in ficante:
        for k in conhecido:
            
            classes = [lista[:] for lista in classes_iniciais]
            
            # Model Selection
            model = ep.SIRModel(grafo)

            # Model Configuration
            config = mc.Configuration()
            config.add_model_parameter("beta", valores[i][0])
            config.add_model_parameter("gamma", valores[i][1])
            # config.add_model_parameter("fraction_infected", 0.01)
            config.add_model_initial_configuration("Infected", [k])

            for (u, v, data) in grafo.edges(data=True):
                weight = data['weight']
                config.add_edge_configuration((u, v), 'threshold', 2 * valores[i][0] * (14 - weight ) / 13)

            model.set_initial_status(config)

            # Simulation execution
            model.set_initial_status(config)
            num_iteracoes = 100
            iterations = model.iteration_bunch(num_iteracoes)

            suscetiveis = []
            infectados = []
            recuperados = []
            
            for a in classes:
                if k in a:
                    a.remove(k)
            
            # status: 0 - suscetível, 1 - infectado, 2 - recuperado
            for j in iterations:
                # suscetiveis.append(j['node_count'][0])
                # infectados.append(j['node_count'][1])
                # recuperados.append(j['node_count'][2])
                for x in j['status']:
                    if j['status'][x]==1:
                        if x in classes[0]:
                            classes[0].remove(x)
                            # if(len(classes[0])==0):
                            #     classes_infectado[0].append(j['iteration'])
                        
                        elif x in classes[1]:
                            classes[1].remove(x)
                            # if(len(classes[1])==0):
                            #     classes_infectado[1].append(j['iteration'])
                                
                        elif x in classes[2]:
                            classes[2].remove(x)
                            # if(len(classes[2])==0):
                            #     classes_infectado[2].append(j['iteration'])
                                
                        elif x in classes[3]:
                            classes[3].remove(x)
                            # if(len(classes[3])==0):
                            #     classes_infectado[3].append(j['iteration'])
                                
                        elif x in classes[4]:
                            classes[4].remove(x)
                            # if(len(classes[4])==0):
                            #     classes_infectado[4].append(j['iteration'])
                                
                        elif x in classes[5]:
                            classes[5].remove(x)
                            # if(len(classes[5])==0):
                            #     classes_infectado[5].append(j['iteration'])
                                
                        elif x in classes[6]:
                            classes[6].remove(x)
                            # if(len(classes[6])==0):
                            #     classes_infectado[6].append(j['iteration'])
                                
                        elif x in classes[7]:
                            classes[7].remove(x)
                            # if(len(classes[7])==0):
                            #     classes_infectado[7].append(j['iteration'])
                                
                        elif x in classes[8]:
                            classes[8].remove(x)
                            # if(len(classes[8])==0):
                            #     classes_infectado[8].append(j['iteration'])
                                
                        elif x in classes[9]:
                            classes[9].remove(x)
                            # if(len(classes[9])==0):
                            #     classes_infectado[9].append(j['iteration'])
                                
                        elif x in classes[10]:
                            classes[10].remove(x)
                            # if(len(classes[10])==0):
                            #     classes_infectado[10].append(j['iteration'])
                                
                        elif x in classes[11]:
                            classes[11].remove(x)
                            # if(len(classes[11])==0):
                            #     classes_infectado[11].append(j['iteration'])
                                
                        elif x in classes[12]:
                            classes[12].remove(x)
                            # if(len(classes[12])==0):
                            #     classes_infectado[12].append(j['iteration'])
            # 
            
            pos = 0
            for a in classes:
                if(classes_tamanho[pos]!=0):
                    porcentagem = ((classes_tamanho[pos]- len(a))*100)/classes_tamanho[pos]
                    porcentagem_infectados[pos].append(porcentagem)
                pos+=1
            
            
            
            # plt.plot(suscetiveis, label='Suscetíveis')
            # plt.plot(infectados, label='Infectados')
            # plt.plot(recuperados, label='Recuperados')
            # plt.xlabel('Iterações')
            # plt.ylabel('Nós')
            # plt.legend(loc='best')
            # plt.title(f'beta: {valores[i][0]}, gamma: {valores[i][1]}, nó_inicial: {k}')
            # plt.show()
        
        # print(f'soma: {sum(iteracao_infectado)} | len: {len(iteracao_infectado)}')
        # media = sum(iteracao_infectado) / len(iteracao_infectado)
        # print(media)
        
        for a in porcentagem_infectados:
            if(len(a)==0):
                a.append(0)
        
        # print(porcentagem_infectados)
        print(f'porcentagem familia: {sum(porcentagem_infectados[0])/len(porcentagem_infectados[0])}')
        print(f'porcentagem melhor amigo: {sum(porcentagem_infectados[1])/len(porcentagem_infectados[1])}')
        print(f'porcentagem namorada: {sum(porcentagem_infectados[2])/len(porcentagem_infectados[2])}')
        print(f'porcentagem amigo: {sum(porcentagem_infectados[3])/len(porcentagem_infectados[3])}')
        print(f'porcentagem parente: {sum(porcentagem_infectados[4])/len(porcentagem_infectados[4])}')
        print(f'porcentagem parca: {sum(porcentagem_infectados[5])/len(porcentagem_infectados[5])}')
        print(f'porcentagem professor: {sum(porcentagem_infectados[6])/len(porcentagem_infectados[6])}')
        print(f'porcentagem aluno: {sum(porcentagem_infectados[7])/len(porcentagem_infectados[7])}')
        print(f'porcentagem colega: {sum(porcentagem_infectados[8])/len(porcentagem_infectados[8])}')
        print(f'porcentagem trabalho: {sum(porcentagem_infectados[9])/len(porcentagem_infectados[9])}')
        print(f'porcentagem consanguineo: {sum(porcentagem_infectados[10])/len(porcentagem_infectados[10])}')
        print(f'porcentagem ficante: {sum(porcentagem_infectados[11])/len(porcentagem_infectados[11])}')
        print(f'porcentagem conhecido: {sum(porcentagem_infectados[12])/len(porcentagem_infectados[12])}')
        
        # for a in classes_infectado:
        #     if(len(a)==0):
        #         a.append(0)
        # print(classes_infectado)
        
        # print(f"media familia: {sum(classes_infectado[0])/len(classes_infectado[0])}")
        # print(f"media melhor amigo: {sum(classes_infectado[1])/len(classes_infectado[1])}")
        # print(f"media namorado: {sum(classes_infectado[2])/len(classes_infectado[2])}")
        # print(f"media amigo: {sum(classes_infectado[3])/len(classes_infectado[3])}")
        # print(f"media parente: {sum(classes_infectado[4])/len(classes_infectado[4])}")
        # print(f"media parca: {sum(classes_infectado[5])/len(classes_infectado[5])}")
        # print(f"media professor: {sum(classes_infectado[6])/len(classes_infectado[6])}")
        # print(f"media aluno: {sum(classes_infectado[7])/len(classes_infectado[7])}")
        # print(f"media colega: {sum(classes_infectado[8])/len(classes_infectado[8])}")
        # print(f"media trabalho: {sum(classes_infectado[9])/len(classes_infectado[9])}")
        # print(f"media consanguineo: {sum(classes_infectado[10])/len(classes_infectado[10])}")
        # print(f"media ficante: {sum(classes_infectado[11])/len(classes_infectado[11])}")
        # print(f"media conhecido: {sum(classes_infectado[12])/len(classes_infectado[12])}")