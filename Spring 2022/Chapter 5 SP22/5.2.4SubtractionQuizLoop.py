import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions asked
NUMBER_OF_QUESTIONS = 5 # Constant

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:  # 5 question limit
    # Generate two random single digit integers
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the user to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " - " +
                        str(number2) + "? "))

    # Grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1

    else:
        print("Your answer is wrong.\n", number1, "-",
              number2, "is", number1 - number2)

    # Increase the count (number of questions asked)
    count += 1

endTime = time.time() # Get the end time
testTime = int(endTime - startTime) # Get the test time
print("Correct count is", correctCount, "out of",
      NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")