# Receba um número inteiro positivo na entrada e imprima os 
# n primeiros números ímpares naturais. Para a saída, siga o 
# formato do exemplo abaixo.

# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

num = int(input('Digite o valor de n: '))
impar = 1

while num != 0:
    print(impar)
    impar+=2
    num-=1
