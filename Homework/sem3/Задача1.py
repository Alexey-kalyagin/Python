# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.  

import random

n = int(input('Введите значение размера списка N: '))
listN = []
sum = 0

for elem in range(n):
    listN.append(random.randint(0,n))

for j in range(len(listN)):
    if j%2>0:
        sum+= listN[j]
       
print(listN) 
print(sum)