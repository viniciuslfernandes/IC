opcao_arquivo = input("Digite 1 para visualizar o grafo de Gabriel ou 2 para visualizar o grafo de Vinicius ou 3 para um grafo Generico: \n")

if opcao_arquivo == '1':
    arquivo = './gabriel/conexoes.txt'
elif opcao_arquivo == '2':
    arquivo = './vinicius/conexoes_vinicius.txt'
elif opcao_arquivo == '3':
    arquivo = './generico.txt'
else:
    print("Opção de arquivo inválida")
    exit()

with open(arquivo, 'r') as f:
    linhas = f.readlines()

pesos_atualizado = []
for i in linhas:
    v1, v2, peso = i.split()
    peso = int(peso)
    
    if(peso == 2 or peso == 3 or peso == 4):
        peso = 1
    elif(peso == 5 or peso == 6 or peso == 7 or peso == 8 or peso == 9 or peso == 10):
        peso = 2
    elif(peso == 11 or peso == 12 or peso == 13):
        peso = 3
    pesos_atualizado.append(f"{v1} {v2} {peso}\n")

with open('./gabriel/conexoes2.txt', 'w') as f:
    f.writelines(pesos_atualizado)
    