import random
from pathlib import Path

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    r"""
     _______
     |     |
     |
     |
     |
     |
   __|__
""",
    r"""
     _______
     |     |
     |     O
     |
     |
     |
   __|__
""",
    r"""
     _______
     |     |
     |     O
     |     |
     |
     |
   __|__
""",
    r"""
     _______
     |     |
     |     O
     |    /|
     |
     |
   __|__
""",
    r"""
     _______
     |     |
     |     O
     |    /|\
     |
     |
   __|__
""",
    r"""
     _______
     |     |
     |     O
     |    /|\
     |    /
     |
   __|__
""",
    r"""
     _______
     |     |
     |     O
     |    /|\
     |    / \
     |
   __|__
""",
]

DEFAULT_WORDS = [
    "python", "computer", "security", "forensics", "network",
    "keyboard", "programming", "internet", "firewall", "database",
    "encryption", "software", "algorithm", "evidence", "password",
]


def load_words():
    """Load words from words.txt if it exists; otherwise use built-in words."""
    word_file = Path(__file__).with_name("words.txt")

    if word_file.exists():
        try:
            words = [
                line.strip().lower()
                for line in word_file.read_text(encoding="utf-8").splitlines()
                if line.strip().isalpha() and len(line.strip()) >= 3
            ]
            if words:
                return words
        except OSError:
            print("Could not read words.txt. Using the built-in word list.")

    return DEFAULT_WORDS


def display_game(secret_word, guessed_letters, wrong_guesses):
    """Display the current gallows, masked word, and guessed letters."""
    print(HANGMAN_STAGES[wrong_guesses])

    masked_word = " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:             ", masked_word)
    print("Wrong attempts:   ", f"{wrong_guesses}/{MAX_ATTEMPTS}")
    print("Guessed letters:  ", " ".join(sorted(guessed_letters)).upper() or "None")


def get_guess(guessed_letters):
    """Ask for one valid letter that has not already been guessed."""
    while True:
        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. Try another letter.")
        else:
            return guess


def play_game(words):
    """Run one complete round of Hangman."""
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n" + "=" * 38)
    print("          H A N G M A N")
    print("=" * 38)
    print(f"Guess the hidden word! You have {MAX_ATTEMPTS} incorrect attempts.")

    while wrong_guesses < MAX_ATTEMPTS:
        display_game(secret_word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 38)
            print("          YOU WIN!")
            print(f"   Great job! The word was: {secret_word.upper()}")
            print("=" * 38)
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess.upper()}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry! '{guess.upper()}' is not in the word.")

    display_game(secret_word, guessed_letters, wrong_guesses)
    print("\n" + "=" * 38)
    print("          GAME OVER!")
    print(f"   The correct word was: {secret_word.upper()}")
    print("=" * 38)


def main():
    words = load_words()

    while True:
        play_game(words)
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
