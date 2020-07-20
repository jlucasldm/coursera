# Refaça o exercício 1 imprimindo os retângulos sem 
# preenchimento, de forma que os caracteres que não 
# estiverem na borda do retângulo sejam espaços

# digite a largura: 10
# digite a altura: 3
# ##########
# #        #
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
        if i == 0 or i == alt-1:
            print("#", end='')
        else:
            if j == 0 or j == larg - 1:
                print("#", end='')
            else:
                print(' ', end='')
        j += 1
    
    print('')
    i += 1
