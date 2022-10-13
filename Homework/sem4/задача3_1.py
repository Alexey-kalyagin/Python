d = input('Введите последовательность цифр: ')
size = 0
elem = d
k = d
e = 0
a = 0

while d>0:
    size+=1
    d//=10

new = []

for i in range(size):
    e = int(elem%10)
    elem = int(elem/10)
    new.append(e)

new.reverse()
print(new)