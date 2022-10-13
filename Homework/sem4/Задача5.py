# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.




firstEquation = r"/home/alexey/Рабочий стол/git/python/Homework/sem4/mnogochlen1.txt"                   # присваиваем переменной значение импортируемой функции
secondEquation = r"/home/alexey/Рабочий стол/git/python/Homework/sem4/mnogochlen2.txt"

data = open(firstEquation,"r")
for line1 in data:
    print (line1)


equation1 = {}

firstEquation = line1.replace(" + "," +").replace(" - "," -").split()[:-2]    # разбиваем наше уравнение на элементы списка ( [:-2] для удаления последних двух элементов списка"=0")

for i in range(len(firstEquation)):
    firstEquation[i] = firstEquation[i].replace(" + ", "").split("x^")       # разбиваем единый список на списки состоящие из двух элементов (число и степень)
    
    equation1[int(firstEquation[i][1])] = int(firstEquation[i][0])            # переводим список в словарь, где ключом задаём степень числа, а элементом число нашего многочлена

print(equation1)


data = open(secondEquation,"r")
for line2 in data:
    print (line2)

equation2 = {}

secondEquation = line2.replace(" + "," +").replace(" - "," -").split()[:-2]    # разбиваем наше уравнение на элементы списка ( [:-2] для удаления последних двух элементов списка"=0")

for i in range(len(secondEquation)):
    secondEquation[i] = secondEquation[i].replace(" + ", "").split("x^")       # разбиваем единый список на списки состоящие из двух элементов (число и степень)
    equation2[int(secondEquation[i][1])] = int(secondEquation[i][0]) 

print(equation2)

sumEquations = {}

for i in range(max(len(equation1), len(equation2)), -1, -1):                  # перебираем элементы от максимального ключа с шагом -1
    first = equation1.get(i)
    second = equation2.get(i)
    if first != None or second != None:
        sumEquations[i] = (first if first != None else 0) + (second if second != None else 0)  # складываем элементы с идентичными ключами

strings = ''

for i in range(len(sumEquations), -1, -1):
    strings += str(sumEquations.get(i)) + 'x^' + str(i) + '+'

strings = strings.replace("+Nonex^1","").replace("+Nonex^5","") + '=0'
sum = strings.replace('+=', '=').replace('+-','-').replace('x^0', '')
print()

print(sum)

data = open(r"/home/alexey/Рабочий стол/git/python/Homework/sem4/sum_mnogochlen.txt", "w") 
data.write (f'Сумма многочленов = {sum} \n')
data.close
