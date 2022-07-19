# This code gives you the max number inputed out of all of the inputs
number = eval(input("Enter an integer: "))
max = number

while number != 0:
    number = eval(input("enter in integer: "))
    if number > max:
        max = number

print("max is", max)
print("number", number)