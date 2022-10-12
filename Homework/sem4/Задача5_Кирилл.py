# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


from Задача4 import createEquation                      # импортируем ф-ию из задачи4

def readEquation():                                     # создаём ф-ю
    firstEquation = createEquation()                    # присваиваем переменной значение импортируемой функции
    eqation = {}


    firstEquation = firstEquation.replace(" + "," +").replace(" - "," -").split()[:-2]    # разбиваем наше уравнение на элементы списка ( [:-2] для удаления последних двух элементов списка"=0")

    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace(" + ", "").split("x^")       # разбиваем единый список на списки состоящие из двух элементов (число и степень)
        eqation[int(firstEquation[i][1])] = int(firstEquation[i][0])            # переводим список в словарь, где ключом задаём степень числа, а элементом число нашего многочлена

    return eqation

word1 = readEquation()
word2 = readEquation()

finalWord = {}

for i in range(max(len(word1), len(word2)), -1, -1):                  # перебираем элементы от максимального ключа с шагом -1
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)  # складываем элементы с идентичными ключами

print(word1)
print(word2)
print(finalWord)