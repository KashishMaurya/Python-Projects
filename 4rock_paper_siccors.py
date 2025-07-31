import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_elements = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

try:
    user_choice = int(input("Your choice: "))
    if user_choice < 0 or user_choice > 2:
        print("❌ Invalid choice. You must enter 0 for Rock, 1 for Paper, or 2 for Scissors.")
    else:
        computer_choice = random.randint(0, 2)

        print(f"\n🧍 You chose:\n{game_elements[user_choice]}")
        print(f"\n🤖 Computer chose:\n{game_elements[computer_choice]}")

        # Result logic
        if user_choice == computer_choice:
            print("⚔️ It's a draw.")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("✅ You win!")
        else:
            print("❌ You lose.")
except ValueError:
    print("❗ Invalid input. Please enter a number (0, 1, or 2).")
