import random

# Generate a number to be guessed
number = random.randint(1, 100)

print("Guess a magic number between 0 and 100")

guess = -1 # This value is used to initially start the loop
while guess != number:
    # Prompt the user to guess the number
    guess = eval(input("Enter your guess: "))

    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
        