 # Создайте программу для игры в 'Крестики-нолики'.


pos = []

for i in range(1,10):
    pos.append(i)

count = 0
player = '0'

while True:
    if count %2 == 0:
        player = "X"
    else:
        player = "0"
  
    print(f"|{pos[0]:^5}|{pos[1]:^5}|{pos[2]:^5}|")
    print("-------------------")
    print(f"|{pos[3]:^5}|{pos[4]:^5}|{pos[5]:^5}|")
    print("-------------------")
    print(f"|{pos[6]:^5}|{pos[7]:^5}|{pos[8]:^5}|")
    
    index = int(input(f"\n\nХод {'Player1' if player == 'X' else 'Player2'}: "))
    
    if pos[index-1] == "0" or pos[index-1] == "X":
        print("Ход недопустим") 
        
    else:
        pos[index-1] = player
        count+=1

    if pos[0] == pos[1] == pos[2] == "X" or pos[3] == pos[4] == pos[5] == "X" or pos[6] == pos[7] == pos[8] == "X":
        print('Player1 win') 
        break
    if pos[0] == pos[3] == pos[6] == "X" or pos[1] == pos[4] == pos[7] == "X" or pos[2] == pos[5] == pos[8] == "X":
        print('Player1 win') 
        break
    if pos[0] == pos[4] == pos[8] == "X" or pos[2] == pos[4] == pos[6] == "X":
        print('Player1 win') 
        break
            
    if pos[0] == pos[1] == pos[2] == "0" or pos[3] == pos[4] == pos[5] == "0" or pos[6] == pos[7] == pos[8] == "0":
        print('Player2 win') 
        break
    if pos[0] == pos[3] == pos[6] == "0" or pos[1] == pos[4] == pos[7] == "0" or pos[2] == pos[5] == pos[8] == "0":
        print('Player2 win') 
        break
    if pos[0] == pos[4] == pos[8] == "0" or pos[2] == pos[4] == pos[6] == "0":
        print('Player2 win')  
        break  
    
    if count > 8:
        print("Ничья")   
        break
    