# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

listCtr = ['абв', 'рпоид', 'апрабвшл', 'ерл', 'шрлжз']

NewList = []

print(listCtr) 

for i in range(len(listCtr)):
    findElem = listCtr[i].find('абв')
    if findElem == -1:
        NewList.append(listCtr[i]) 
print(f"Cписок без элементов 'абв' - {NewList}")       

