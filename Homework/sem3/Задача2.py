# Напишите программу, которая айдёт произведение пар чисел списка
# (Списщк создаётся, как в предыдущем задании). 
# Парой считаем первый и последний эл-тб второй и предпоследний и т.д.

import random

n = int(input('Введите значение размера списка N: '))
listN = []
k = n-1
sum1 = 0
#sum2 = 0
#sum3 = 0
#sum4 = 0 
#sum5 = 0

for elem in range(n):
    listN.append(random.randint(0,n))

print(listN) 
#print (k)
for j in range(len(listN)):
    
    if j < k:
        sum1= listN[j]*listN[k]
        k -=1
        print(sum1)
       

#print(sum1)