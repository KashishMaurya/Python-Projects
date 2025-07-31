import random

def set_difficulty(difficulty): 
    """Set the difficulty and guesses"""
    if difficulty == 'easy':
        print("You have 10 attempts to guess the number.")
        t_guesses = 10
    elif difficulty == 'hard':
        print("You have 5 attempts to guess the number.")
        t_guesses = 5
    else:
        print("Invalid difficulty level, defaulting to easy mode.")
        t_guesses = 10
        
    return t_guesses
    

def check_guess(number, t_guesses): 
    while t_guesses > 0:
        guess = input("Try guessing the number! : ")
        
        if guess.isdigit():
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue  # don't consume guess count for invalid input
            elif guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("🎉 Congratulations! You have guessed the number!")
                return
            t_guesses -= 1
            if t_guesses > 0:
                print(f"You have {t_guesses} guesses left.") 
        else:
            print("Please enter a valid number.")
            
    print(f"❌ You've run out of guesses. The number was {number}.")


# main  
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
      
number = random.randint(1, 100)

chances = set_difficulty(difficulty)

check_guess(number, chances)
