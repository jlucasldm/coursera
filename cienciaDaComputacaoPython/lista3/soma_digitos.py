# Escreva um programa que receba um número inteiro na entrada, 
# calcule e imprima a soma dos dígitos deste número na saída
# Exemplo:
# Digite um número inteiro: 123
# 6

num = int(input('Digite um número inteiro: '))
soma = 0

while num != 0:
    if num<0:
        num*=-1
    var = num%10
    soma+=var
    num = num//10

print(soma)