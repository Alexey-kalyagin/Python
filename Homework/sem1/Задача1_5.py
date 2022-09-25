# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

M = int(input('Введите размер поля: '))
N = int(input('Введите № четверти: '))

if N==1:

    for i in range(1, M+1):
        for j in range(1, M+1):
            print(f'x = {i}  y= {j}')

elif N==2:
    for i in range(-M, 0):
        for j in range(1, M+1):
            print(f'x = {i}  y= {j}')

elif N==3:
    for i in range(-M, 0):
        for j in range(-M, 0):
            print(f'x = {i}  y= {j}')

elif N==4:
    for i in range(1, M+1):
        for j in range(-M, 0):
            print(f'x = {i}  y= {j}')
