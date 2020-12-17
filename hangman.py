# Project 5 - HANGMAN

import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)  # the word we are trying to guess
    word_letters = set(word)   # creates a dictionary of unique letters in word
    alphabet = set(string.ascii_uppercase) # dictionary of all upper case letters
    used_letters = set()
    lives = 6

    print(f'\nOK, the computer has chosen a {len(word)}-letter word. Time for you to start guessing!')
    print(f'\nYou get {lives} chances should you make an incorrect guess!')
    # get user input
    while len(word_letters) > 0 and lives > 0:
        if len(used_letters) > 0:
            print('\nSo far, you have chosen the following letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('\nCurrent word: ', ' '.join(word_list))
        user_letter = input('\nEnter a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print()
            else:
                lives -= 1
                if lives == 1:
                    text = 'guess'
                else:
                    text = 'guesses'
                print(f'\nIncorrect! You have {lives} incorrect {text} left!')
        elif user_letter in used_letters:
            print('\nYou have already entered that letter!')
        else:
            print('\nYou have entered that an invalid guess - try again with a letter!')
    if lives == 0:
        print(f'\nHard luck, the correct answer was {word}. Better luck next time!')
    elif len(word_letters) == 0:
        if lives == 1:
            text = 'guess'
        else:
            text = 'guesses'
        print(f'\nAwesome, you guessed the word ({word}) correctly and still had {lives} {text} left!')

hangman()
