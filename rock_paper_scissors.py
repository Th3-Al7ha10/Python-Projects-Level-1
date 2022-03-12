"""
Pierre Papier Ciseaux (Rock Paper scissors)

Created on Mon Feb 28, 2022

@author: Th3-Al7ha10


"""

import random

def chifoumi():
    choice = random.randint(1,3)
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissors'
    
def play():
    player_choice = 0
    
    while (player_choice != 1 and player_choice != 2 and player_choice !=3):
        try:
            player_choice = int(input('Press 1 for "Rock", 2 for "Paper" and 3 for "Scissors"'))
            break
        except:
            print("That's not a valid option!")     
    if player_choice == 1:
        return 'Rock'
    elif player_choice == 2:
        return 'Paper'
    else:
        return 'Scissors'
    
def winner(x, y):
    choices = []
    choices.append(x)
    choices.append(y)
    if 'Rock' and'Paper' in choices:
        return 'Paper'
    elif 'Rock' and'Scissors' in choices:
        return 'Rock'
    elif 'Rock' and'Paper' in choices:
        return 'Scissors'
    

print("Welcome to the game Rock Paper Scissors! \n Let's play!")

boole = 1
score_player = 0
score_computer = 0

while boole:

     computer = chifoumi()
     player = play()

     print ('You choose:{} and the computer:{}'.format(player,computer))
     if winner(computer,player) == player:
        score_player+=1 
        print("You win")
     elif winner(computer,player) == computer:
         score_computer+=1
         print("You loose")
     else:
         print("Even")
     next_round = input('Do you want to play another round?1. Yes / 0. No')
     if next_round == 1:
         boole = 1
     else:
         boole = 0
     

print ('Game Over!\n Final Score: Player {} Computer {}'.format(score_player,score_computer))



    
