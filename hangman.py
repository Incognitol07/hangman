import random as rn
import pyfiglet
word_list = [
    "abyss",
    "askew",
    "awkward",
    "avenue",
    "banjo",
    "bayou",
    "blitz",
    "bookworm",
    "boxcar",
    "buckaroo",
    "buffalo",
    "buzzing",
    "cobweb",
    "crypt",
    "cycle",
    "faking",
    "fixable",
    "glowworm",
    "gossip",
    "haiku",
    "haphazard",
    "icebox",
    "jazzy",
    "jigsaw",
    "joking",
    "lucky",
    "matrix",
    "numbskull",
    "onyx",
    "pajama",
    "pixel",
    "puppy",
    "quartz",
    "queue",
    "quorum",
    "rhythm",
    "scratch",
    "snazzy",
    "staff",
    "stretch",
    "subway",
    "swivel",
    "topaz",
    "unzip",
    "uptown",
    "walkway",
    "waltz",
    "wave",
    "waxy",
    "wimpy",
    "woozy",
    "yippee",
    "zigzag",
    "zombie"
]



chosen_word=rn.choice(word_list)
ascii_art = pyfiglet.figlet_format("hangman", font='big')
stages=[
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
"""]

display=[]
for letters in chosen_word:
    display+="_"
lives=5
print(ascii_art)
print(chosen_word)
while True:
    guess=input("Guess a letter: ")
    if guess in display:
        print(f"You've already guessed {guess}")
    guess=guess.lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{"_".join(display)}")
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives-=1
        if lives==0:
            print(stages[0])
            print("Oh no! The hangman has met his fate. Better luck next time!")
            break
    
    if "_" not in display:
        print("Hooray! You saved the hangman!")
        break
    print(stages[lives])
