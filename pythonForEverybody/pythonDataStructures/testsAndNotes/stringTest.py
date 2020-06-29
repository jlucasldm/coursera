fruit = 'banana'

for letter in fruit:
    print(letter)

print('')
print('second way')
print('')

index = 0
while index <len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print('')
print('next example')
print('')

s = 'Monty Python'
print(s[0:4])   #up but not including 4
print(s[6:7])   #up but not including 7
print(s[6:20])  #up but not including 20

print('')

print(s[:2])    #up but not including 2
print(s[8:])    #starting at 8
print(s[:])     #full string