import random as rn
import pyfiglet
import os

word_list = [
    "abyss", "askew", "awkward", "avenue", "banjo", "bayou", "blitz", "bookworm",
    "boxcar", "buckaroo", "buffalo", "buzzing", "cobweb", "crypt", "cycle",
    "faking", "fixable", "glowworm", "gossip", "haiku", "haphazard", "icebox",
    "jazzy", "jigsaw", "joking", "lucky", "matrix", "numbskull", "onyx", "pajama",
    "pixel", "puppy", "quartz", "queue", "quorum", "rhythm", "scratch", "snazzy",
    "staff", "stretch", "subway", "swivel", "topaz", "unzip", "uptown", "walkway",
    "waltz", "wave", "waxy", "wimpy", "woozy", "yippee", "zigzag", "zombie"
]

chosen_word = rn.choice(word_list)
ascii_art = pyfiglet.figlet_format("hangman", font='big')
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
win=    """
    +---+
    |   |
        |
    O   |
   /|\\  |
   / \\  |
===========
"""

display = ["_" for _ in chosen_word]
lives = 5
print(ascii_art)

while True:
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        print(stages[lives])
        print(f"You've already guessed {guess}")
        continue
    
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        print(stages[lives])
        print(f"Wow!, '{guess}' is definitely in the word")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        print(stages[lives])
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
    
    
    if "_" not in display:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        print(f"{' '.join(display)}")
        print(win)
        print("Hooray! You saved the hangman!")
        break
    
    if lives == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_art)
        print(stages[0])
        print("Oh no! The hangman has met his fate. Better luck next time!")
        print(f"The word was '{chosen_word}'.")
        break
