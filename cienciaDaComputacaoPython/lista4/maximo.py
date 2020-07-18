def maximo(x, y):
    if x >= y:
        return x
    else:
        return y

num1 = int(input('poe um numero ai: '))
num2 = int(input('poe outro ai: '))

print(maximo(num1, num2))
