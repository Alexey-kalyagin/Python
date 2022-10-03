#Реализуйте алгоритм перемешивания списка

import random

listA = []
for i in range(5):
    listA.append(int(input('Введите число ')))

print(listA)

random.shuffle(listA)

print(listA)