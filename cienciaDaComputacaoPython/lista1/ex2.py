# Faça um programa em Python que receba quatro notas, calcule 
# e imprima a média aritmética. Observe o exemplo abaixo:
## Entrada de Dados: ##
# Digite a primeira nota: 4
# Digite a segunda nota: 5
# Digite a terceira nota: 6
# Digite a quarta nota: 7
## Saída de Dados: ##
#A média aritmética é 5.5

prim = input('Digite a primeira nota:')
seg = input('Digite a segunda nota:')
terc = input('Digite a terceira nota:')
quar = input('Digite a quarta nota:')

media = (int(prim) + int(seg) + int(terc) +int(quar))/4

print('A média aritmética é', media)
