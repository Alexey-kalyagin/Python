# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

N = float(input('Введите число для проверки: '))

print(f'число кратно 5? - {(N%5)==0}')
print(f'число кратно 10? - {(N%10)==0}')
print(f'число кратно 15? - {(N%15)==0}')
print(f'число не кратно 30? - {(N%30)!=0}')

# if N%5 ==0 and N%10 ==0 or N%15 ==0 and N%30 !=0:
#    print ('Верно')