# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = float(input('Введите число N: '))
listN = []
count = 2
while n > 2:
    if n%count!=0:
        count+=1
            
    else:
        n//=count
        listN.append(count)
        
print(listN)

