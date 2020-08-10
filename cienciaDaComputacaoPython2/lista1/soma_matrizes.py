def dimensoes(matriz):
    tam_i = 0
    tam_j = 0
    for i in matriz:
        tam_i += 1
        for j in i:
            if tam_i == 1:
                tam_j += 1
    return tam_i, tam_j

def soma_matrizes(m1, m2):
    if dimensoes(m1) != dimensoes(m2):
        return False
    linhas = 0
    colunas = 0
    for i in m1:
        linhas += 1
        for j in i:
            if linhas == 1:
                colunas+=1
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(m1[i][j]+m2[i][j])
        matriz.append(linha)
    print(matriz)
    return matriz