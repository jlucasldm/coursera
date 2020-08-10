def dimensoes(matriz):
    tam_i = 0
    tam_j = 0
    for i in matriz:
        tam_i += 1
        for j in i:
            if tam_i == 1:
                tam_j += 1
    print(tam_i, end="")
    print("X", end="")
    print(tam_j)
