import random

WORDS = ["python", "hangman", "function", "variable", "developer"]
MAX_GUESSES = 6


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_GUESSES:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_GUESSES}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Wrong! ({wrong_guesses}/{MAX_GUESSES})\n")

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
