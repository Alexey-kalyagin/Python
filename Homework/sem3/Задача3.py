# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и 
# засчитывать 0 как минимальное не стоит
# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

listA = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(5):
    listA[i]=listA[i]%1 

print(listA) 

max = listA[0]
for i in listA:
    if i>max: 
        max=i
print(max)

min = listA[0]
for i in listA:
    if 0<i<min: 
        min=i
print(min)

result = round(max-min, 2)
print(result)