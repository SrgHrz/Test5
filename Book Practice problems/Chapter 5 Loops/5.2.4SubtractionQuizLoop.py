import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 5 # Constant

startTime = time.time() # Gets the start time

while count < NUMBER_OF_QUESTIONS: # Limits the number of questions to 5
    # Generate two random single digit numbers
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # If number1 < number2 , swap
    if number1 < number2:
        number1, number2 = number2, number1

        # Prompt the student to answer "What is number1 - number2?"
        answer = eval(input("What is " + str(number1) + " - " +
                            str(number2) + "?"))

        # Grade number and display the result
        if number1 - number2 == answer:
            print("You are correct!")
            correctCount += 1 # Simultaneously adds and reassigns the variable " correct count" to a new number
        else:
            print("Your answer is wrong.\n", number1, " - ",
                  number2, "is", number1 - number2)

        # Increase the count
        count += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of",
      NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")