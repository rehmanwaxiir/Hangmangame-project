"""
Hangman Game
Guess the word one letter at a time before running out of attempts.
"""
import random

WORDS = ["python", "hangman", "computer", "keyboard", "developer", "programer"]

def play():
    word = random.choice(WORDS)
    guessed = set()
    attempts_left = 6

    print("Welcome to Hangman!\n")

    while attempts_left > 0:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in word:
            attempts_left -= 1
            print("Wrong guess!")

        if all(letter in guessed for letter in word):
            print(f"\nYou won! The word was '{word}'.")
            return

    print(f"\nOut of attempts! The word was '{word}'.")

if __name__ == "__main__":
    play()
