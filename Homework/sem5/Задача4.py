# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

#Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

d = input('Введите число d: ')

listD = []
newlistD = []
for i in d:
    listD.append(i)
print(d)

def Numb(listD):
    for i in range(len(listD)-1):
        if listD[i].isdigit():
            if listD[i+1].isdigit():
                n = int(listD[i])*10 + int(listD[i+1])
                k = n*listD[i+2]
            else:
                n = int(listD[i])
                k = n*listD[i+1]
            
            newlistD.append(k)  
    return newlistD
def Str(listD):
    count = 1
    for i in range(len(listD)-1): 
        if listD[i]==listD[i+1]:
            count+=1
        else:
            newlistD.append(count)
            newlistD.append(listD[i])
            count = 1   
    return newlistD

if listD[0].isdigit():
    Numb(listD)
else:
    Str(listD)


print("".join(map(str,newlistD)))