# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

N = input('Введите число: ')

N = N.replace('.','')
sum = 0

for i in N:
   
    int_lst = [int(i) for i in N]
    
for i in int_lst:    
    
    sum = sum + i 

print (sum)


# Решение Кирилла
# N = input('Введите число: ')
# sum = 0
# for i in N:
#   if i.isdigit()
#       sum += int(i)
# print(sum)




    
