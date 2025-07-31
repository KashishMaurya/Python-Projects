import random

# Extended word list
word_list = [
    "challenge", "purple", "elephant", "biscuit", "notebook", "umbrella",
    "giraffe", "computer", "python", "keyboard", "internet", "library",
    "window", "mountain", "pencil", "science", "glasses", "backpack", "river"
]

# Hangman ASCII art stages
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(word_list)

# def display_progress(word, guessed_letters):
#     return ''.join([letter if letter in guessed_letters else '_' for letter in word])
# simplified one :
def display_progress(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result

def hangman():
    word = choose_word()
    guessed_letters = []
    lives = 6

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You have 6 lives. Each wrong guess draws more of the hangman.")
    print(hangman_stages[0])
    print(display_progress(word, guessed_letters))

    while lives > 0:
        guess = input("Guess a letter: ").lower()

        # not a alphabet of entered multiple chars
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            lives -= 1
            print("Wrong guess.")
            print(f"Lives left: {lives}")
            if lives == 1:
                print("Last chance!")

        print(hangman_stages[6 - lives])
        progress = display_progress(word, guessed_letters)
        print("Current word: " + progress)

        if "_" not in progress:
            print("\nCongratulations! You won!")
            print(f"The word was: {word}")
            break

        else:
            print(hangman_stages[6])
            print("\nGame over!")
            print(f"The word was: {word}")


# Start the game
hangman()
