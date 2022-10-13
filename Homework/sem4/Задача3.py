# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


from random import randint

unicum = {}
finalStr = ''

d = input('Введите последовательность цифр: ')


for i in d:
    if unicum.get(i):
        unicum[i] = unicum.get(i)+1
    else:
        unicum[i] = 1

for i in unicum.items():
    if i[1] == 1:
        finalStr+=str(i[0])
print (f'Уникальные цифры {finalStr}') if finalStr else print('Уникальных позиций нет')


