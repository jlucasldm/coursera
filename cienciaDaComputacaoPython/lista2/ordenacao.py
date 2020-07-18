#Receba 3 números inteiros na entrada e imprima
#crescente
#se eles forem dados em ordem crescente. Caso contrário, imprima
#não está em ordem crescente

pri = int(input('primeiro numero'))
seg = int(input('segundo numero'))
ter = int(input('terceiro numero'))

if pri<seg and seg<ter:
    print('crescente ', pri, seg, ter)
else:
    print('não está em ordem crescente ', pri, seg, ter)