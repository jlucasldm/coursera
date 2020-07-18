def maior_primo(x):
    n = 2
    while n <= x:
        i = 2
        flag = 0

        while i<n:
            if n%i == 0:
                flag=1
            i+=1
        if flag == 0:
            bigger = n
        n+=1
    return bigger

num = int(input('poe numero ai: '))

print(maior_primo(num))
