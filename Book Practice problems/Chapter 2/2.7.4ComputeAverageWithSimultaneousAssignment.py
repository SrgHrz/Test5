# Prompt the user to enter 3 numbers
number1, number2, number3 = eval(input("Enter three numbers"
                                       "seperated by commas: "))

# Compute average
average = (number1 + number2 + number3) / 3
print("The average of", number1, number2, number3, "is", average)