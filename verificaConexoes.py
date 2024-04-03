def verifica_vertice_invertido(v, v1, v2):
    for vertice in v:
        if vertice[0] == v2 and vertice[1] == v1:
            return True
    return False

if __name__ == '__main__':
    arquivo = './conexoes.txt'
    naoExiste = './naoExiste.txt'
    v = []
    peso = []

    with open(naoExiste, 'w') as e:
        with open(arquivo, 'r') as f:
            for linha in f:
                novaLinha = linha.strip()
                num1 = novaLinha.split(' ')[0]
                num2 = novaLinha.split(' ')[1]
                num3 = novaLinha.split(' ')[2]
                v.append((num1,num2))
                peso.append(num3)

        for vertice in v:
            if not verifica_vertice_invertido(v, vertice[0], vertice[1]):
                e.write(f'{vertice[1]} {vertice[0]} {peso[v.index(vertice)]}\n')