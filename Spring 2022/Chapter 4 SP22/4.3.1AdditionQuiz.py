import random

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Prompt the user to enter an answer
# Recall what we are doing here is using the string
# concentration operator!!! +
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

# Display Result
print(number1, "+", number2, "=", answer,  # The answer part is what you input
      "is", number1 + number2 == answer)  # This will either be true or false