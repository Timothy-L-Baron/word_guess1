"""create an original word guessing game without using resources specifically regarding how to make guess word games (hangman, etc) - only use resources
about loops, lists, variables, etc"""

#import module
import random

#create a list of words to guessing
words = ['ketchup', 'mustard', 'green', 'yellow', 'cordial', 'spaniel', 'worker', 'information', 'jasper', 'science']

#create a list for wrong guess letters
guessed_letters = []

#create a function to choose a random word from the 'words' list and turn it into a series of blanks (a blank for each letter)
def create_guess_word():
    guess_word = random.choice(words)
    print(guess_word)
    x = guess_word
    return x

#create a function to turn the guess_word into spaces so the user sees a blank word to start
def create_spaced_word(guess_word):
    count = 0
    for letter in guess_word:
        count = count + 1
        spaced_word = (('_') * count)
    print(spaced_word)
    return spaced_word

# create a function to prompt user for a guess a letter
def prompt_user_guess():
    guess_letter = input("Please guess a letter: ").lower()
    return guess_letter

# create a function that determines the indices for all places the guess_letter appears in the guess word, convert the guess_word string into a list, use the indices
#to replace correectly guessed letters with those letters in the list [instead of the blanks], change it back into a string, and print out the results to the user
#if a wrong letter is guessed, return a list of wrong guesses and re-prompt the user
#when the word is fully guessed, stop the program and tell the user he/she won
def guess_letter_in_guess_word(guess_word, guess_letter, spaced_word):
    while True:
        if guess_letter in guess_word:
            index_finder = [n for n in range(len(guess_word)) if guess_word.find(guess_letter, n) == n]
            for index in index_finder:
                list_convert = list(spaced_word)
                list_convert[index] = guess_letter
                spaced_word = "".join(list_convert)
            if spaced_word == guess_word:
                print('You guessed it. You WIN!!!')
                False
                break
            print(spaced_word)
        if guess_letter not in guess_word:
            guessed_letters.append(guess_letter)
            print('That letter is not in the word!')
            print('Your wrong guesses so far: ')
            print(guessed_letters)
            guess_letter = input("Please guess a letter: ").lower()
        else:
            guess_letter = input("Please guess a letter: ").lower()


# use functions and nesting to call the main function
get_word = create_guess_word()
space = create_spaced_word(get_word)
get_guess = prompt_user_guess()
guess_letter_in_guess_word(get_word, get_guess, space)
