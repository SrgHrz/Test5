# This one asks the question until you get it right
# and then the program terminates

import random

# 1. Generate two random single digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
#    b/c you will subtract 1 from 2
if number1 < number2:
    number1 , number2 = number2, number1

# 3. Prompt the student to answer "What is number1 - number2?"
answer = eval(input("What is " + str(number1) + " - "
                    + str(number2) + "? "))

# 4. Repeatedly ask the question until the answer is correct
while number1 - number2 != answer:
    answer = eval(input("Wrong answer. Try again. What is "
            + str(number1) + " - " + str(number2) + "? "))

print("You got it")


