# Escreva um programa que receba um número inteiro na entrada 
# e verifique se o número recebido possui ao menos um dígito 
# com um dígito adjacente igual a ele. Caso exista, imprima 
# "sim"; se não existir, imprima "não".

# Digite um número inteiro: 12345
# não

num = int(input('Digite um número inteiro: '))
flag = 0
antes = 10

while num != 0:
    var = num%10

    if antes == var:
        flag = 1
        break

    antes = var
    num = num//10

if flag == 1:
    print('sim')
else:
    print('não')

