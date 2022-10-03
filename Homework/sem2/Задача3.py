#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


N = int(input('Введите число n: '))

result = {}

sum = 0

for i in range(1,N+1):
    
    result[i] = round((1+1/i)**i, 3)
    sum = round(sum + result[i], 3)

print (result)

print (sum)
    