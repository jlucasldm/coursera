# Escreva um programa que recebe como entradas (utilize a 
# função input) dois números inteiros correspondentes à 
# largura e à altura de um retângulo, respectivamente. O 
# programa deve imprimir uma cadeia de caracteres que 
# represente o retângulo informado com caracteres '#' na 
# saída

# digite a largura: 10
# digite a altura: 3
# ##########
# ##########
# ##########

# digite a largura: 2
# digite a altura: 2
# ##
# ##

larg = int(input('digite a largura: '))
alt = int(input('digite a altura: '))

i = 0
j = 0
while i != alt:
    j = 0
    while j != larg:
        print("#", end='')
        j+=1
    print('')
    i+=1
