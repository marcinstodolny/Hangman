import random
import string
import sys
from pathlib import Path


class hangman:
    def __init__(self):
        self.letters_lowercase = string.ascii_lowercase
        self.read_words_from_file()
        self.word_to_guess = []
        self.used_letters = []
        self.user_choice = ""

    def read_words_from_file(self):
        with open(
            str(Path(__file__).parent.absolute()) + "\\" + "countries.txt"
        ) as words:
            self.word_list = words.readlines()

    def main(self):
        self.get_menu_input_and_check()
        self.set_difficulty_level()
        self.create_word_and_hide_it()
        self.game()

    def get_menu_input_and_check(self):
        while self.user_choice not in ["1", "2", "3"]:
            self.user_choice = input(
                "1. Easy\n2. Medium\n3. Hard\nq. Quit\nChose dificulty(1/2/3/quit): "
            ).lower()
            self.valid_menu_input_or_quit()

    def valid_menu_input_or_quit(self):
        if self.user_choice in ["quit", "q"]:
            print("Good-bye")
            sys.exit()
        elif self.user_choice not in ["1", "2", "3"]:
            print("Invalid input value, try again")

    def set_difficulty_level(self):
        match self.user_choice:
            case "1":
                self.difficulty = self.word_list[:113]
                self.lives = 6
            case "2":
                self.difficulty = self.word_list[114:173]
                self.lives = 8
            case "3":
                self.difficulty = self.word_list[174:242]
                self.lives = 10
        self.show_lives_and_ussed_letters()

    def create_word_and_hide_it(self):
        self.word = random.choice(self.difficulty)[:-1]
        self.create_word_with_underscores(list(self.word))

    def create_word_with_underscores(self, word_list):
        for item in word_list:
            if item == " ":
                self.word_to_guess.append(" ")
            else:
                self.word_to_guess.append("_")

    def game(self):
        while self.word != "".join(self.word_to_guess):
            self.show_state_of_hidden_word()
            self.get_user_input_or_quit()
            self.check_if_user_input_is_correct_or_repeat()
            self.check_if_letter_is_in_the_hidden_word()
            self.check_if_the_game_is_lost()
            self.show_lives_and_ussed_letters()
        self.show_victory_message()

    def show_state_of_hidden_word(self):
        print(" ".join(self.word_to_guess))

    def get_user_input_or_quit(self):
        self.user_choice = input("Enter a letter or 'quit': ").lower()
        if self.user_choice == "quit":
            print("Good-bye")
            sys.exit()

    def check_if_user_input_is_correct_or_repeat(self):
        while (
            self.user_choice in self.used_letters
            or self.user_choice not in self.letters_lowercase
            or self.user_choice == ""
        ):
            self.show_lives_and_ussed_letters()
            self.letter_already_on_list_check()
            self.entered_invalid_value_check()
            self.get_user_input_or_quit()
        self.used_letters.append(self.user_choice)

    def letter_already_on_list_check(self):
        if self.user_choice in self.used_letters:
            print("This letter was already used")
            self.show_state_of_hidden_word()

    def entered_invalid_value_check(self):
        if self.user_choice not in self.letters_lowercase or self.user_choice == "":
            print("You input wrong value")
            self.show_state_of_hidden_word()

    def check_if_letter_is_in_the_hidden_word(self):
        found_index = [
            item
            for item, found in enumerate(self.word)
            if self.user_choice == found.lower()
        ]
        self.convert_underscore_into_valid_letter(found_index)
        if not found_index:
            self.lives -= 1

    def convert_underscore_into_valid_letter(self, found_index):
        for item in found_index:
            self.word_to_guess[item] = self.word[item]

    def check_if_the_game_is_lost(self):
        if self.lives <= 0:
            self.show_hangman_picture()
            print(f"You lost the game\nYour word was: {self.word}")
            sys.exit()

    def show_victory_message(self):
        self.show_state_of_hidden_word()
        print("Good job thats your's word :)")

    def show_lives_and_ussed_letters(self):
        self.show_hangman_picture()
        print(f"Lives left: {self.lives}\nLetters already used: {self.used_letters}")

    def show_hangman_picture(self):
        hangman = [
            """    +---+
    O   |
   /|\  |
   / \  |
       ===""",
            """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
            """
    +---+
    O   |
   /|\  |
        |
       ===""",
            """
    +---+
    O   |
   /|   |
        |
       ===""",
            """
    +---+
    O   |
    |   |
        |
       ===""",
            """
    +---+
    O   |
        |
        |
       ===""",
            """
    +---+
        |
        |
        |
       ===""",
            """    
        |
        |
        |
       ===""",
            """
       ===""",
            "",
            "",
            "",
            "",
            "",
        ]
        print(hangman[self.lives])


hang = hangman()
hang.main()
