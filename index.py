import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
count = 0
max_attempts = 7
won = False

while count < max_attempts:

    # Get a valid number from the user
    while True:
        try:
            guess = int(input("Take a guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Count only valid guesses
    count += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You've guessed the number {secret_number} correctly!")
        print(f"It took you {count} guesses.")
        won = True
        break

# Player didn't win
if not won:
    print("Sorry! You've run out of attempts.")
    print(f"The number was {secret_number}.")