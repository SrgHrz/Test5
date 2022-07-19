import random # imports random numbers module

# 1 Generate two single digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2 If number1 < number2 --> swap
if number1 < number2:
    number1, number2 = number2, number1 # simultaneous assignment

# 3 promp the student to answer "What is number1 - number2?"
answer = eval(input("What is "+ str(number1) + "-" +
                    str(number2) + "?"))

# Check the answer and display the result
if number1 - number2 == answer:
    print("You are corrrect!")
else:
    print("Your answer is wrong.\n", number1, '-',
          number2, "is", number1 - number2, '.')