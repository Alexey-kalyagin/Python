# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

# N = input('Введите число: ')

# N = N.replace('.','')
# sum = 0

# for i in N:
   
#     int_lst = [int(i) for i in N]
    
# for i in int_lst:    
    
#     sum = sum + i 

# print (sum)

n = input('Введите число: ')
sum=0
listStr = list(filter(str.isdigit, n))
listNum = (map(int, listStr))
for i in listNum:    
    sum = sum + i 

print(sum)
