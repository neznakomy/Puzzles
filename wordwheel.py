# Project A - WORD WHEEL
# checks a simple list of English words (words.py, suitable enough for testing)
# and finds words in can make using user-specified 9 letters.  One of the
# 9 letters is a must-have in every valid word.  Version 1 with no frills...

import os
from words import words

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def greeting():
    print('\nWelcome to the Word Wheel solver')

def get_main_letter(main_letter):
    x = input('\nPlease enter the main letter that must exist in every word: ').upper()
    main_letter.append(x)
    return main_letter

def get_other_letters(main_letter, other_letters, letters_list):
    other_letters[main_letter[0]] = 1
    letters_list.append(main_letter[0])
    for x in range(8):
        letter = input('\nPlease enter the other 8 letters that must exist in every word: ').upper()
        if letter not in other_letters:
            other_letters[letter] = 1
            letters_list.append(letter)
        else:
            other_letters[letter] += 1
    return other_letters, letters_list

def display_wordwheel(main_letter, letters_list):
    cls()
    print(f'\nOK, the main letter is {main_letter} and the list of all different letters is: {letters_list}')

def get_check_word(main_letter, other_letters, letters_list):
    total_word_count = valid_word_count = 0
    min_letters = 3
    matching_words = []
    must_have = main_letter[0]
    long_word = ''
    print('\nChecking for words that match...')
    for word in words:
        word = word.upper()
        total_word_count += 1
        tmp = {}    #  for each candidate word we will keep count of letter usage
        contains_invalid = False
        if must_have in word:
            for i in word:
                if i in letters_list:
                    tmp[i] = 1 if i not in tmp else tmp[i] + 1  # update letters counts
                    if tmp[i] > other_letters[i]:  # trap too many uses of allowed letters
                        contains_invalid = True
                else:
                    contains_invalid = True
            if contains_invalid is False and len(word) >= min_letters:  # minimum of 3 letters
                long_word = ' ' if len(word) != 9 else ' * this is a 9-letter word!'
                print(word, long_word)
                matching_words.append(word)
                valid_word_count += 1
    print(f'\nLocated {valid_word_count} words out of a total dictionary of {total_word_count} words')
    return matching_words

def wordwheel():
    cls()
    greeting()

    main_letter = []
    other_letters = {}
    letters_list = []
    matching_words = []

    get_main_letter(main_letter)
    get_other_letters(main_letter, other_letters, letters_list)
    display_wordwheel(main_letter, letters_list)
    get_check_word(main_letter, other_letters, letters_list)

if __name__ == '__main__':
    wordwheel()
