# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.  

import random

# n = int(input('Введите значение размера списка N: '))
# listN = []
# sum = 0

# for elem in range(n):
#     listN.append(random.randint(0,n))

# for j in range(len(listN)):
#     if j%2>0:
#         sum+= listN[j]

n = int(input('Введите значение размера списка N: '))
listN = []
sum = 0
listN=[random.randint(0,n) for _ in range(n)]
print(listN)
listN=[listN[i] for i in range(len(listN)) if i%2 != 0]
print(listN)
for i in listN:
    sum +=i 
print(sum)