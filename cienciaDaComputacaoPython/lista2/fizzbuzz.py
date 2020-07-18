# Receba um número inteiro na entrada e imprima
#FizzBuzz
#se o número for divisível por 3 e por 5. Caso contrário, imprima o 
# mesmo número que foi dado na entrada.

num = int(input('mande o xesque no dele:'))

if num%3==0 and num%5==0 and num !=0:
    print('FizzBuzz')
else:
    print(num)