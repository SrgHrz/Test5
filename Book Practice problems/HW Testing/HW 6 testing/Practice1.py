# Guess Number
number = 1458
print("Welcome to the guessing game. You have ten tries to guess my number.")
count = 0 # Counts the number of attempts
NUMBER_OF_GUESSES = 10 # Max number of attempts


while count < NUMBER_OF_GUESSES:
    # Prompt the user to guess the number
    guess = eval(input("Please enter your guess: "))

    if guess == number:
        print("That's correct!")
        print("Congratulations! you guessed in in your first try. X guesses")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    count += 1
print("Game over: You ran out of guesses")
