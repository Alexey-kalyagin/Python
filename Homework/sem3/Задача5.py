#  Задайте число - размер списка. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Введите число: '))

def fib(n):
    if n in [-k,-k-1]:
        return -1
    elif n in [0,1]:
        return 1
    elif n in [-1,0]:
        return 0
    else:
        return fib(n-1)+fib(n-2)

listFib = []

for e in range(-k,k):
    listFib.append(fib(e))
print(listFib) 

