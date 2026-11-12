# Task 1 – Hangman Game

## Description
A Python-based interactive word guessing game where players try to guess a hidden word one letter at a time within a limited number of attempts.

## Features
- Random word selection
- Letter-by-letter guessing
- Tracks correct and incorrect guesses
- Displays remaining attempts
- Prevents repeated guesses
- Win and lose messages
- Option to play again

## Technologies Used
- Python
- Random Module
- Pathlib Module
- Loops and Conditional Statements
- Functions

## Project Structure
```text
Task_1_Hangman/
│
├── hangman.py
└── README.md
```

## How to Run
1. Open the project folder in a terminal.
2. Run the following command:

```bash
python hangman.py
```

## How to Play
1. The game selects a random hidden word.
2. Guess one letter at a time.
3. Correct guesses reveal the letter in the word.
4. Incorrect guesses reduce your remaining attempts.
5. Guess the complete word before using all six attempts to win.
