def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat*n
        n-=1
    return fat

num = int(input('poe um numero ai man: '))
print(fatorial(num))