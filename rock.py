# Project 4 - ROCK PAPER SCISSORS

import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper or 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'The computer chooses... {computer}')
    if user == computer:
        return('It is a tie')
# r beats s, p beats r, s beats p
    if is_win(user, computer):
        return('You won!')
    else:
        return('You lost!')

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
       (player == 'p' and opponent == 'r') or \
       (player == 's' and opponent == 'p'):
       return(True)

print(play())
