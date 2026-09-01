import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("🎮 Rock, Paper, Scissors Game!")

while True:
    player = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower().strip()

    if player == "quit":
        break

    if player not in choices:
        print("❌ Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("🤝 It's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")
        player_score += 1

    else:
        print("😢 You lose!")
        computer_score += 1

    print(f"Score → You: {player_score} | Computer: {computer_score}")

print("\nGame Over!")
print(f"Final Score → You: {player_score} | Computer: {computer_score}")