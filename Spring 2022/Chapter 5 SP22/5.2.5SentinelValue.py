# A common technique to control a loop is to designate a
# special input value known as a sentinel value which
# signifies the end of an input
# A loop that uses a sentinel value is known as a sentinel controlled loop

data = eval(input("Enter an integer (the input ends " + "if it is 0): "))

# Keep reading data until input is 0
sum = 0
while data != 0:
    sum += data

    data = eval(input("Enter an integer (the input ends " + "if it is 0): "))

print("The sum is", sum)


