import random

print("====================================")
print("     ROCK PAPER SCISSORS GAME")
print("====================================")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\nChoose one:")
    print("Rock")
    print("Paper")
    print("Scissors")

    user_choice = input("\nEnter your choice: ").lower().strip()

    # Check valid input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer random choice
    computer_choice = random.choice(choices)

    # Display choices
    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    # Display scores
print("\n------- SCORE -------")
print("Your Score:", user_score)
print("Computer Score:", computer_score)
print("---------------------")

# Play again
play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

if play_again != "yes":
    print("\n==============================")
    print("        FINAL SCORE")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer is the overall winner!")
    else:
        print("The game ended in a tie!")

    print("Thanks for playing!")
    print("==============================")
