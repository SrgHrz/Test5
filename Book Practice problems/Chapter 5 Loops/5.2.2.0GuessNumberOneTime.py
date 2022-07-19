import random
# This program only lets you enter your guess only once
# Generate a random number to be guessed
number = random.randint(0, 100)

print("Guess a magic number between 0 and 100")

# Prompt the user to guess the number
guess = eval(input("Enter your guess: "))

if guess == number:                      # If the guess = # print the following:
    print("Yes, the number is", number)
elif guess > number:                     # If the guess is > # print the following:
    print("Your guess is too high")
else:                                    # If the following prior conditions aren't met, print the following:
    print("Your guess is too low")