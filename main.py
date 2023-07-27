import re
import time

MAX_TRIES = 7

hangman_photos = {
    1: """         x-------x""",
    2: """          x-------x
          |
          |
          |
          |
          |""",
    3: """                x-------x
                |       |
                |       0
                |
                |
                |""",
    4: """                x-------x
                |       |
                |       0
                |       |
                |
                |""",
    5: """                x-------x
                |       |
                |       0
                |      /|\\
                |
                |""",
    6: """                x-------x
                |       |
                |       0
                |      /|\\
                |      /
                |""",
    7: """            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |"""
}

def show_welcome_popup():
    print("Welcome to Hangman Game!\n\n")
    print("""  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                     |___/\n""")
    print("You have", MAX_TRIES, "tries to guess the word.")
    print("Good luck!")

def get_valid_letter():
    while True:
        letter = input("\nPlease enter a letter: \n").strip().lower()
        if re.match(r'^[a-z]$', letter):
            return letter
        else:
            print("Invalid input. Please enter a single letter.\n")

def display_letters_chosen(letters_list):
    print("\n\n-----------------------------------\nLetters chosen: ==> ",
          " ".join(letters_list), "\n-----------------------------------\n")

def initialize_word(word):
    return "_" * len(word)

def update_word(word, chosen_word, letter):
    new_word = ""
    for w, c in zip(word, chosen_word):
        new_word += c if c != "_" else letter if w == letter else "_"
    return new_word

def run_game():
    word = input("\nPlease enter a word: ").strip().lower()
    chosen_letters = []
    guessed_word = initialize_word(word)
    attempts = 0
    MAX_TRIES = 7

    while MAX_TRIES > 0:
        display_letters_chosen(chosen_letters)
        print("Current word:\n", guessed_word)

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:\n", word)
            break

        letter = get_valid_letter()
        time.sleep(0.5)

        if letter in chosen_letters:
            print("You already chose this letter. Try again.\n")
        else:
            chosen_letters.append(letter)
            if letter in word:
                guessed_word = update_word(word, guessed_word, letter)
            else:
                MAX_TRIES -= 1
                attempts += 1
                print("**************"*10, "\n")
                print("Incorrect letter. You have", MAX_TRIES, "tries left.\n")
                print("Your status:\n------------ \n\n")
                print(hangman_photos[attempts])
    if MAX_TRIES == 0:
        print("Game over!\nThe word was: ", word)

if __name__ == "__main__":
    show_welcome_popup()
    run_game()
