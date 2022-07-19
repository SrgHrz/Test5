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

# 4 Repeatedly ask the question until the answer is correct (!= means loop runs as long as answer is incorrect) (!=) = not equal to
while number1 - number2 != answer:
    answer = eval(input("Wrong answer. Try again. What is "
                        + str(number1) + " - " + str(number2) + "?"))

print("You got it")
