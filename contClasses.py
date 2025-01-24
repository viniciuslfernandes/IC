opcao_arquivo = input("Digite 1 para visualizar o grafo de Gabriel ou 2 para visualizar o grafo de Vinicius ou 3 para um grafo Generico: \n")

if opcao_arquivo == '1':
    arquivo = './gabriel/conexoes2.txt'
elif opcao_arquivo == '2':
    arquivo = './vinicius/conexoes2_vinicius.txt'
elif opcao_arquivo == '3':
    arquivo = './generico_seir.txt'
else:
    print("Opção de arquivo inválida")
    exit()

with open(arquivo, 'r') as f:
    linhas = f.readlines()

tam = [0, 0, 0]
for i in linhas:
    v1, v2, peso = i.split()
    peso = int(peso)
    v1 = int(v1)
    if(v1==1 and peso==1):
        tam[0]+=1
    elif(v1==1 and peso==2):
        tam[1]+=1
    elif(v1==1 and peso==3):
        tam[2]+=1
    
print(tam)