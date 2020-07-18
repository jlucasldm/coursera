# Escreva um programa que receba um número inteiro positivo 
# na entrada e verifique se é primo. Se o número for primo, 
# imprima "primo". Caso contrário, imprima "não primo".

# Exemplos:
# Digite um número inteiro: 13
# primo

while 1 == 1:
    num = input('Digite um número inteiro: ')
    
    if num == 'sai':
        break

    num = int(num)
    i = 2
    flag = 0

    while i<num:
        if num%i == 0:
            flag=1
        i+=1

    if flag == 0 and num > 1:
        print('primo')
    else:
        print('não primo')