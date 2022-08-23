#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('''-----Tic Tac Toe-----
Key in the coordinates of where you want to move.
The coordinates are as follows:
(1 3) (2 3) (3 3)
(1 2) (2 2) (3 2)
(1 1) (2 1) (3 1)
Player X will start first by default.
Have fun!
------------------------------
''')

def game(user_input,user_input2, player):
    try:
        row = int(user_input2[0])
        col = int(user_input2[2])
    except:
        print ("You should enter numbers!")
        return user_input

    if row > 3 or row < 1 or col > 3 or col < 1:
        print("Coordinates should be from 1 to 3!")
        return user_input
    
    elif (row == 1 and col == 1 and user_input[6] != "_") or (row == 1 and col == 2 and user_input[3] != "_") or (row == 1 and col == 3 and user_input[0] != "_") or (row == 2 and col == 1 and user_input[7] != "_") or (row == 2 and col == 2 and user_input[4] != "_") or (row == 2 and col == 3 and user_input[1] != "_") or (row == 3 and col == 1 and user_input[8] != "_") or (row == 3 and col == 2 and user_input[5] != "_") or (row == 3 and col == 3 and user_input[2] != "_"):
        print("This cell is occupied! Choose another one!")
        return user_input
    
    else:
        user_input = list(user_input)
        
        if row == 1 and col == 1:
            user_input[6] = player
        elif row == 1 and col == 2:
            user_input[3] = player
        elif row == 1 and col == 3:
            user_input[0] = player
        elif row == 2 and col == 1:
            user_input[7] = player
        elif row == 2 and col == 2:
            user_input[4] = player
        elif row == 2 and col == 3:
            user_input[1] = player
        elif row == 3 and col == 1:
            user_input[8] = player
        elif row == 3 and col == 2:
            user_input[5] = player
        elif row == 3 and col == 3:
            user_input[2] = player
            
        user_input = ("").join(user_input)
        return user_input
    

def result(old_user_input):
    if user_input[0] == user_input[1] == user_input[2] == "X" or user_input[3] == user_input[4] == user_input[5] == "X" or user_input[6] == user_input[7] == user_input[8] == "X" or user_input[0] == user_input[3] == user_input[6] == "X" or user_input[1] == user_input[4] == user_input[7] == "X" or user_input[2] == user_input[5] == user_input[8] == "X" or user_input[0] == user_input[4] == user_input[8] == "X" or user_input[2] == user_input[4] == user_input[6] == "X":
        print("X wins")
        return False
    elif user_input[0] == user_input[1] == user_input[2] == "O" or user_input[3] == user_input[4] == user_input[5] == "O" or user_input[6] == user_input[7] == user_input[8] == "O" or user_input[0] == user_input[3] == user_input[6] == "O" or user_input[1] == user_input[4] == user_input[7] == "O" or user_input[2] == user_input[5] == user_input[8] == "O" or user_input[0] == user_input[4] == user_input[8] == "O" or user_input[2] == user_input[4] == user_input[6] == "O":
        print("O wins")
        return False
    elif all([x != '_' for x in user_input]):
        print("Draw")
        return False
    else:
        return True

def drawing(user_input):
    user_input = user_input.replace("_", " ")

    print('---------')
    print('| ' + user_input[0] + ' ' + user_input[1] + ' ' + user_input[2] + ' |')
    print('| ' + user_input[3] + ' ' + user_input[4] + ' ' + user_input[5] + ' |')
    print('| ' + user_input[6] + ' ' + user_input[7] + ' ' + user_input[8] + ' |')
    print('---------')
    
def initialization():
    global user_input
    user_input = "_________"
    old_user_input = user_input
    drawing(user_input)
    
    players = ["X", "O"]
    counter = 0
    
    while result(old_user_input) == True:
        if counter % 2 == 0:
            player = players[0]
        else: 
            player = players[1]
        
        while old_user_input == user_input:
            user_input2 = input("Enter the coordinates: > " )
            user_input = game(old_user_input, user_input2, player)
            
        else:
            counter += 1
            old_user_input = user_input
            drawing(user_input)

initialization()
input('Press ENTER to exit')


# In[ ]:




