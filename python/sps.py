import random
import math
from enum import Enum
import time
import sys


class sps(Enum):
    Stone = 1
    Paper = 2
    Scissors = 3


print('•'.ljust(50, '•'))
print('🎮'.ljust(25, '🎮'))
title = '👊✋✌️ Stone Paper scissors 👊✋✌️'.upper()
print('🎮' + title.center(44, "•") + '🎮')
print('🎮'.ljust(25, '🎮'))
print('•'.ljust(50, '•'))
print('\n\n')
u = int(input(
    'Choose and enter \n 1 For Stone \n 2 For Paper \n 3 For Scissors\n Enter VALUE'.center(100)))
print('\n\n')
if u > 3:
    sys.exit('''
             you Betrayed
             🐍 is going back
             GOOD BYE
❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌'''.upper())
print('Now its 🐍\'s turn (it is blindfolded-so don\'t worry about cheating)')
time.sleep(2)
python = int(random.choice('123'))
print('🐍 chose ' + str(sps(python)).replace('sps.', ' '))
print('\n\n')

print('•'.ljust(50, '•'))
print('\n')
if u == python:
    print("Uff! SAME LUCK....IT\'s a TIE 👔".center(50))
elif u == 1 | python == 3:
    print('Hurray! You Won 🎉🎉'.upper().center(50))
elif u == 2 | python == 1:
    print('Hurray! You Won 🎉🎉'.upper().center(50))
elif u == 3 | python == 2:
    print('Hurray! You Won 🎉🎉'.upper().center(50))
else:
    print('''        👅😏 YOU LOSE
VICTORY TIME FOR 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍''')
