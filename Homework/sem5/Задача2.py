# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random 


candies = int(input("Введите количество конфет, сладкоежки: " ))
candiesPl1 = 0
candiesPl2 = 0
count = random.randint(1,6)
print(f"Пока в карзине {candies} конфет") 
print()
print(f"На костях выполо {count}")
print()

if candies>0:
    while True:
        if count %2 == 0:
            print("Ходит Player1") 
            print()
            player = int(input("Сколько хочешь взять конфет? - " )) 
            print()
            if player<=20:
                candiesPl1 += player
                candies -= player
                count+=1
                if candies<=0:
                       
                    if count%2!=0:
                        print ("Player1 win")
                        break
                    else:
                        print ("Player2 win")
                        break
            else:
                print("Слишком много конфет, жадина)")
            
        else:
            print("Ходит Player2") 
            print()
            player = int(input("Сколько хочешь взять конфет? - " )) 
            print()
            if player<=20:
                candiesPl2 += player
                candies -= player
                count+=1
                if candies<=0:
                    if count%2!=0:
                        print ("Player1 win")
                        break
                    else:
                        print ("Player2 win")
                        break
            else:
                print("Слишком много конфет, жадина)")
           
        print(f"Конфеты первого игрока {candiesPl1}")
        print(f"Конфеты второго игрока {candiesPl2}")
        print(f"Остаток конфет {candies}")
        print()




        # index = int(input(f"\n\nХод {'Player1' if player == 'X' else 'Player2'}: "))