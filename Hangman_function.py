import random
import string
import sys
from pathlib import Path
letters_lowercase = string.ascii_lowercase
countries = str(Path(__file__).parent.absolute())
words = open((countries+ '\\' + "countries.txt")).readlines()
word_easy = words[:113]
word_medium = words[114:173]
word_hard = words[174:242]
level = 0
lives = 0
word_to_guess = []
used_letters = []
word = ""


def main():
    user_choice = ""
    while user_choice not in ["1", "2", "3"]:
        user_choice = input(
            "1. Easy\n2. Medium\n3. Hard\nq. Quit\nChose dificulty(1/2/3/quit): ")
        if user_choice == "q":
            sys.exit()
        if user_choice not in ["1", "2", "3"]:
            print("Invalid input value, try again")
    match user_choice:
        case "1":
            level = word_easy
            lives = 6
        case "2":
            level = word_medium
            lives = 7
        case "3":
            level = word_hard
            lives = 10
    word_to_show = random.choice(level)[:-1]
    word = list(word_to_show)
    for item in word:
        if item == " ":
            word_to_guess.append(" ")
        else:
            word_to_guess.append("_")
    word = "".join(word)
    game(user_choice, lives, word, word_to_guess)


def game(user_choice, lives, word, word_to_guess):
    while True:
        print(" ".join(word_to_guess))
        user_choice = input("Enter a letter or 'quit': ").lower()
        while user_choice in used_letters or user_choice not in letters_lowercase:
            if user_choice == "quit":
                print("Good-bye")
                sys.exit()
            show_state_of_game(lives, used_letters)
            if user_choice in used_letters:
                print(f"This letter is already on the list\n{' '.join(word_to_guess)}")
                
            if user_choice not in letters_lowercase:
                print(f"You input wrong value\n{' '.join(word_to_guess)}")
            user_choice = input("Enter a letter or 'quit': ").lower()
        used_letters.append(user_choice)
        if found_index := [item for item, found in enumerate(word) if user_choice == found.lower()]:
            for item in found_index:
                if item == 0:
                    word_to_guess[item] = user_choice.upper()
                elif list(word)[item - 1] == " ":
                    word_to_guess[item] = user_choice.upper()
                else:
                    word_to_guess[item] = user_choice
        else:
            lives -= 1
            if lives <= 0:
                print(f"{''.join(Hangman[lives])}\nYou lost the game\nYour word was: {word}")
                sys.exit()
        if word.lower() == "".join(word_to_guess).lower():
            print(f"{' '.join(word_to_guess)}\nGood job thats yours word :)")
            sys.exit()
        show_state_of_game(lives, used_letters)


def show_state_of_game(lives, used_letters):
    hang = "".join(Hangman[lives])
    print(f"{hang}\nLives left: {lives}\nLetters used: {str(used_letters)}")

Hangman = [
    '''    +---+
    O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
        |
        |
        |
       ===''', '''    
        |
        |
        |
       ===''', '''
       ===''', '', '', '', '', ''
]
main()
