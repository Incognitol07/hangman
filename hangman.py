import random as rn
import pyfiglet
import os

# List of possible words for the hangman game
word_list = [
    "abyss", "askew", "awkward", "avenue", "banjo", "bayou", "blitz", "bookworm",
    "boxcar", "buckaroo", "buffalo", "buzzing", "cobweb", "crypt", "cycle",
    "faking", "fixable", "glowworm", "gossip", "haiku", "haphazard", "icebox",
    "jazzy", "jigsaw", "joking", "lucky", "matrix", "numbskull", "onyx", "pajama",
    "pixel", "puppy", "quartz", "queue", "quorum", "rhythm", "scratch", "snazzy",
    "staff", "stretch", "subway", "swivel", "topaz", "unzip", "uptown", "walkway",
    "waltz", "wave", "waxy", "wimpy", "woozy", "yippee", "zigzag", "zombie"
]

# Randomly select a word from the list
chosen_word = rn.choice(word_list)

# Generate ASCII art for the game title using pyfiglet
ascii_art = pyfiglet.figlet_format("hangman", font='big')

# Stages of the hangman game
stages = [
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
===========
""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
===========
""", """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
    |   |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
        |
        |
        |
===========
""", """
    +---+
    |   |
        |
        |
        |
        |
===========
"""
]

# Winning screen art
win = """
    +---+
    |   |
        |
    O   |
   /|\\  |
   / \\  |
===========
"""

# Initialize the display with blanks and set lives
display = ["_" for _ in chosen_word]
lives = 6

# Clear the terminal screen
os.system('clear' if os.name == 'posix' else 'cls')

# Print the initial game setup
print(ascii_art)
print(stages[lives])

# List to track guessed letters
choices = []

# Main game loop
while True:
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    
    if guess in choices:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(ascii_art)
        print(stages[lives])
        print(f"You've already guessed '{guess}'")
    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        os.system('clear' if os.name == 'posix' else 'cls')
        print(ascii_art)
        print(stages[lives])
        print(f"Wow!, '{guess}' is definitely in the word")
    else:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(ascii_art)
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
    choices.append(guess)
    
    # Check if the game is won
    if "_" not in display:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(ascii_art)
        print(f"{' '.join(display)}")
        print(win)
        print("Hooray! You saved the hangman!")
        break
    
    # Check if the game is lost
    if lives == 0:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(ascii_art)
        print(stages[0])
        print("Oh no! The hangman has met his fate. Better luck next time!")
        print(f"The word was '{chosen_word}'.")
        break
