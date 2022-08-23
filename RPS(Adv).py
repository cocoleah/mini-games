#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

#Get Username
# name = input("Enter your name: > ")
# print("Hello,", name)

#Get Game options (https://www.umop.com/rps15.htm)
options_avail = ['gun','rock','fire','scissors','snake','human','tree','wolf','sponge','paper','air','water','dragon','devil','lightning']

game_dic = {'rock': ['fire', 'scissors', 'snake', 'human', 'wolf', 'sponge', 'tree'], 
            'fire': ['scissors','paper','snake','human','tree','wolf','sponge'], 
            'scissors': ['air','tree','paper','snake','human','wolf','sponge'],
            'snake': ['human','wolf','sponge','tree','paper','air','water'],
            'human': ['tree', 'wolf','sponge','paper','air','water','dragon'],
            'tree': ['wolf','dragon','sponge','paper','air','water','devil'],
            'wolf': ['sponge','paper','air','water','dragon','lightning','devil'],
            'sponge': ['paper','air','water','devil','dragon','gun','lightning'],
            'paper': ['air','rock','water','devil','dragon','gyn','lightning'],
            'air': ['fire','rock','water','devil','gun','dragon','lightning'],
            'water': ['devil','dragon','rock','fire','scissors','gun','lightning'],
            'dragon': ['devil','lightning','fire','rock','scissors','gun','snake'],
            'devil': ['rock','fire','scissors','gun','lightning','snake','human'],
            'lightning': ['gun','scissors','rock','tree','fire','snake','human'],
            'gun': ['rock','tree','fire','scissors','snake','human','wolf']}

options_chosen = []

print("Welcome! \nRefer to https://www.umop.com/rps15.htm for more info about this Rock Paper Scissors (Adv)\n")
print("Please select your elements (min of 3, or else default RPS is given). \nYou can select from:", ','.join(map(str, options_avail)))
print("\nEg of Input: rock,fire,scissors,snake,human")
user_option = input("Input here: ").split(',')

if set(user_option).issubset(options_avail) and len(user_option) >= 3:
    options_chosen = user_option
else:
    options_chosen = ['scissors','paper','rock']
    
print("\nOkay, let's start!")
print("Your available options are: ", options_chosen)
print("Type your element to play. Type !rating to see your score. Type !exit to end game.")
print("+50 points if draw. +100 points if you win. 0 points if you lose.")
user = input()

#Get Score
score = 0
# df = open('rating.txt').read().split('\n')
# scores = []
# names = []

# for i in df:
#     line = i.split(' ')
#     names.append(line[0])
#     scores.append(int(line[1]))
    
# try:
#     score = scores[names.index(name)]
# except:
#     score = 0

#Game Play
def game(user, score):
    computer = random.choice(options_chosen)

    if user in options_chosen and type(user) == str:        
        if user == computer:
            print("There is a draw (", computer, ")")
            score += 50
        elif computer in game_dic.keys() and user in game_dic[computer]:
            print("Sorry, but computer chose", computer)
        else:
            print("Well done. Computer chose", computer, "and failed")
            score += 100
    else:
        print("Invalid input")

    return(score)
    
def initialization(user, score):
        if user == "!rating":
            print("Your rating:", score)
            return score
        else:
            score = game(user, score)
            return score

# try:
#     user = int(user)
# except: 
#     user = user

while user != "!exit":
    score = initialization(user, score)
    user = input() 
    try:
        user = int(user)
    except: 
        user = user
else: 
    print("Bye!", input("Press enter to exit"))

