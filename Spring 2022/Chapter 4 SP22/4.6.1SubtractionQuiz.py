# This program only gives you one shot to answer
# the question

import random

# 1. Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1 # Simultaneous assignment

# 3. Prompt the student to answer "What is number1 - number2?"
answer = eval(input("What is " + str(number1) + " - " +
                    str(number2) + "? " ))

# 4. Check the answer and display the result
if number1 - number2 == answer:
    print("You are correct")
else:
    print("Your answer is wrong.\n", number1, "-",
    number2, "is", number1 - number2, ".")

