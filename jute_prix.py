"""
Juste Prix (The Right Price)

Created on Mon Feb 27, 2022

@author: Th3-Al7ha10

In this game, the user have to guess the right price.

"""


import random

print('''In this game, you have to guess a price from 0 to 100.\n
      You have a score of 100 at the begining which decreases after each wrong try.''')

price = random.randrange(1,100)

guess_number = 101

score = 100

while guess_number != price:
    guess_number = input('Guess the price:')
    
    if guess_number > price:
        print('The price is lower')
    else:
        print('The price is higher')
    score = score-1
    
print('Congrats!!! You just find the right price. \n  Your score on 100 is:',score)
