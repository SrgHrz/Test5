import random
# This program allows you to enter numbers until your guess is correct.
# Generate a random number to be guessed
number = random.randint(0, 100)

print("Guess a magic number between 0 and 100")

guess = -1 # what is the purpose of this -1?, explained in the book
while guess != number:
    # Prompt the user to guess the number
    guess = eval(input("Enter your guess: "))

    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")