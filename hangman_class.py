import random
import string
import sys
from pathlib import Path


class hangman:
    def __init__(self):
        self.letters_lowercase = string.ascii_lowercase
        self.words = open(str(Path(__file__).parent.absolute()) + '\\' + "countries.txt").readlines()
        self.word_easy = self.words[:113]
        self.word_medium = self.words[114:173]
        self.word_hard = self.words[174:242]
        self.level = 0
        self.lives = 0
        self.word_to_guess = []
        self.used_letters = []
        self.word = ""
        self.user_choice = ""

    def game(self):
        while self.user_choice not in ["1", "2", "3"]:
            self.user_choice = input("1. Easy\n2. Medium\n3. Hard\nq. Quit\nChose dificulty(1/2/3/quit): ")
            if self.user_choice.lower() in ["quit", "q"]:
                print("Bye")
                sys.exit()
            elif self.user_choice not in ["1", "2", "3"]:
                print("Invalid input value, try again")
        self.chose_level()
        self.main()
        
    def chose_level(self):
        match self.user_choice:
            case "1":
                self.level = self.word_easy
                self.lives = 6
            case "2":
                self.level = self.word_medium
                self.lives = 7
            case "3":
                self.level = self.word_hard
                self.lives = 10
        self.word = list(random.choice(self.level)[:-1])
        print(f"You have {self.lives} lives good luck :)")
        for item in self.word:
            if item == " ":
                self.word_to_guess.append(" ")
            else:
                self.word_to_guess.append("_")
        self.word = "".join(self.word)
        
    def main(self):
        while self.word.lower() != "".join(self.word_to_guess).lower():
            print(" ".join(self.word_to_guess))
            self.user_choice = input("Enter a letter or 'quit': ").lower()
            self.check_input()
            self.used_letters.append(self.user_choice)
            self.check_letter_in_word()
            print(self.show_state_of_game())
        print(f"{' '.join(self.word_to_guess)}\nGood job thats yours word :)")
        sys.exit()
        
    def check_input(self):
        while self.user_choice in self.used_letters or self.user_choice not in self.letters_lowercase or self.user_choice == "":
            if self.user_choice == "quit":
                print("Good-bye")
                sys.exit()
            print(self.show_state_of_game())
            if self.user_choice in self.used_letters:
                print(f"This letter is already on the list\n{' '.join(self.word_to_guess)}")
            if self.user_choice not in self.letters_lowercase or self.user_choice == "":
                print(f"You input wrong value\n{' '.join(self.word_to_guess)}")
            self.user_choice = input("Enter a letter or 'quit': ").lower()
                
    def check_letter_in_word(self):
        found_index = [item for item, found in enumerate(self.word) if self.user_choice == found.lower()]
        for item in found_index:
            if item == 0 or list(self.word)[item - 1] == " ":
                self.word_to_guess[item] = self.user_choice.upper()
            else:
                self.word_to_guess[item] = self.user_choice
        if not found_index: self.lives -= 1
        if self.lives <= 0:
            print(f"{self.Hangman_picture()}\nYou lost the game\nYour word was: {self.word}")
            sys.exit()

    def show_state_of_game(self):
        return f"{self.Hangman_picture()}\nLives left: {self.lives}\nLetters already used: {self.used_letters}"

    def Hangman_picture(self):
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
        return Hangman[self.lives]
hang = hangman()
print(hang.game())