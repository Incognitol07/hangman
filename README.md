### `README.md`


# Hangman Game

This is a simple command-line Hangman game implemented in Python.

## Features

- Randomly selects a word from a predefined list.
- Displays an ASCII art representation of the game state.
- Tracks guessed letters and remaining lives.
- Clears the screen to update the game state after each guess.

## Requirements

- Python 3.x
- `pyfiglet` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the `hangman.py` script to start the game:
```sh
python hangman.py
```

## How to Play

1. **Objective:** The objective of the game is to guess the hidden word, one letter at a time, before the hangman is completely drawn.

2. **Game Start:** When you start the game, the title "HANGMAN" will be displayed along with the initial state of the hangman.

3. **Guessing Letters:** 
   - You will be prompted to guess a letter.
   - If the guessed letter is in the word, it will be revealed in its correct position(s).
   - If the guessed letter is not in the word, you will lose a life, and part of the hangman will be drawn.

4. **Tracking Progress:**
   - The game will display the current state of the word, showing correctly guessed letters and underscores for remaining letters.
   - It will also show the current state of the hangman and inform you of any repeated guesses.

5. **Winning the Game:** You win the game if you correctly guess all the letters in the word before the hangman is fully drawn.

6. **Losing the Game:** You lose the game if the hangman is fully drawn before you can guess the entire word. The correct word will be revealed.



### `requirements.txt`


pyfiglet
