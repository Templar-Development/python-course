# one of my first projects was hangman
# think i made it just under 5 years ago (https://github.com/cqb13/Python-Hangman/commit/42b545ccf5541ab4603210f10cfdd39315afd81f)
# found it a while ago and made some updates
# https://github.com/cqb13/Python-Hangman

import random

words = ["random", "words", "for", "testing", "purposes", "cur", "sum", "hic"]


def hangman():
    lives = 5
    word = choose_word()
    guessed_letters = []
    correct_letters = []

    while lives > 0:
        print_word(word, guessed_letters)
        print(f"Lives: {lives}")
        guess = input("Guess a letter: ")

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.append(guess)

        if guess in word:
            correct_letters.append(guess)
            print("Correct!")
        else:
            lives -= 1
            print("Incorrect!")

        if len(correct_letters) == len(word):
            print("You win!")
            return


def choose_word():
    return random.choice(words)


def print_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print("\n")


if __name__ == "__main__":
    hangman()
