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

# Dictionary of hints for each word
hints = {
    "abyss": "A deep or seemingly bottomless chasm.",
    "askew": "Not in a straight or level position.",
    "awkward": "Causing difficulty; hard to do or deal with.",
    "avenue": "A broad road in a town or city.",
    "banjo": "A stringed musical instrument with a round body.",
    "bayou": "A marshy outlet of a lake or river.",
    "blitz": "A sudden, intense military attack.",
    "bookworm": "A person devoted to reading.",
    "boxcar": "A railroad freight car.",
    "buckaroo": "A cowboy.",
    "buffalo": "A large, wild ox.",
    "buzzing": "Making a low, continuous humming sound.",
    "cobweb": "A spider's web, especially when old and covered with dust.",
    "crypt": "An underground room or vault beneath a church.",
    "cycle": "A series of events that are regularly repeated.",
    "faking": "Pretending to be something one is not.",
    "fixable": "Capable of being repaired.",
    "glowworm": "A beetle with bioluminescent larvae.",
    "gossip": "Casual or unconstrained conversation about others.",
    "haiku": "A Japanese poem of seventeen syllables.",
    "haphazard": "Lacking any obvious principle of organization.",
    "icebox": "A chilled box for keeping something cold.",
    "jazzy": "Lively, bright, and colorful.",
    "jigsaw": "A puzzle consisting of many small, irregular pieces.",
    "joking": "Making jokes; speaking humorously.",
    "lucky": "Having good fortune.",
    "matrix": "An environment in which something develops.",
    "numbskull": "A foolish or stupid person.",
    "onyx": "A semiprecious stone with layers of different colors.",
    "pajama": "A suit of loose pants and jacket for sleeping.",
    "pixel": "The smallest unit of a digital image.",
    "puppy": "A young dog.",
    "quartz": "A hard, crystalline mineral.",
    "queue": "A line of people or vehicles.",
    "quorum": "The minimum number of members needed for a meeting.",
    "rhythm": "A strong, regular, repeated pattern of movement or sound.",
    "scratch": "To score or mark the surface of something.",
    "snazzy": "Stylish and attractive.",
    "staff": "A group of people working together.",
    "stretch": "To extend or draw out to full length.",
    "subway": "An underground electric railroad.",
    "swivel": "A coupling between two parts enabling one to revolve.",
    "topaz": "A precious stone, typically colorless or yellow.",
    "unzip": "To open the zipper of.",
    "uptown": "The residential area of a city.",
    "walkway": "A passage or path for walking along.",
    "waltz": "A dance in triple time.",
    "wave": "A long body of water curling into an arched form.",
    "waxy": "Having the texture or appearance of wax.",
    "wimpy": "Weak and ineffectual.",
    "woozy": "Unsteady, dizzy, or dazed.",
    "yippee": "An exclamation of delight.",
    "zigzag": "A line or course having abrupt alternate right and left turns.",
    "zombie": "A fictional undead being."
}



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
def hangman_game():
    chosen_word = rn.choice(word_list)
    display = ["_" for _ in chosen_word]
    lives = 6
    choices = []

    # Clear the terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')

    # Generate ASCII art for the game title using pyfiglet
    ascii_art = pyfiglet.figlet_format("hangman", font='big')

    # Print the initial game setup
    print(ascii_art)
    print(stages[lives])

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

        # Provide a hint if lives are reduced to 2
        if lives == 2:
            print(f"Hint: {hints[chosen_word]}")

        # Check if the game is won
        if "_" not in display:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(ascii_art)
            print(f"{' '.join(display)}")
            print(win)
            print("Hooray! You saved the hangman!")
            restart = input("Do you want to start again [y/n]: ")
            if restart.lower() == "y":
                return True
            else:
                print("Thanks for playing!!")
                print("See you next time.")
                return False

        # Check if the game is lost
        if lives == 0:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(ascii_art)
            print(stages[0])
            print("Oh no! The hangman has met his fate. Better luck next time!")
            print(f"The word was '{chosen_word}'.")
            restart = input("Do you want to start again [y/n]: ")
            if restart.lower() == "y":
                return True
            else:
                print("Thanks for playing!!")
                print("See you next time.")
                return False

while hangman_game():
    pass
