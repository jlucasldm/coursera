# Escreva um programa que receba um número natural nn na 
# entrada e imprima n!n! (fatorial) na saída. Exemplo:
# Digite o valor de n: 5
# 120

valor = int(input('Digite o valor de n: '))
produto = 1

while valor!=0:
    produto*=valor
    valor-=1

print(produto)