import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!")
print("Type 'quit' to exit.\n")

while True:
    user = input("Choose rock, paper or scissors: ").lower()

    if user == "quit":
        print("Goodbye!")
        break

    if user not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!\n")
    else:
        print("You lose!\n")
