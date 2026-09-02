import random

print("Rock Paper Scissors Game")
print("--" * 20)
print()


class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0

    def make_choice(self):
        self.choice = input(
            f"{self.name}, enter rock, paper, or scissors: "
        ).lower()


class Computer(Player):
    def make_choice(self):
        self.choice = random.choice(
            ["rock", "paper", "scissors"]
        )


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def decide_winner(self):

        if self.player.choice == self.computer.choice:
            print("It's a tie!")

        elif (
            (self.player.choice == "rock" and self.computer.choice == "scissors")
            or
            (self.player.choice == "paper" and self.computer.choice == "rock")
            or
            (self.player.choice == "scissors" and self.computer.choice == "paper")
        ):
            print("You win!")
            self.player.score += 1

        else:
            print("Computer wins!")
            self.computer.score += 1


# Create objects
player = Player("Player")
computer = Computer("Computer")
game = Game(player, computer)

# Make choices
player.make_choice()
computer.make_choice()

# Show choices
print()
print(f"{player.name} chose: {player.choice}")
print(f"{computer.name} chose: {computer.choice}")

# Decide winner
game.decide_winner()

# Show scores
print()
print(f"{player.name} score: {player.score}")
print(f"{computer.name} score: {computer.score}")