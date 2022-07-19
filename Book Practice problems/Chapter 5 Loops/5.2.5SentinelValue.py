data = eval(input("Enter an integer (the input ends " +
                  "if it is 0: "))

# Keep reading data until the input is zero
sum = 0
while data != 0: # while the input is not equal to zero, loop runs
    sum += data # += adds and simultaneously assigns

    data = eval(input("Enter an integer (the input ends " +
                      "if it is 0: "))

print("The sum is", sum)

# or my way:
data = eval(input("Enter a integer(the input ends if it is 0: "))

# Keep reading data until input is 0
sum = 0
while data != 0:
    sum += data

    data = eval(input("Enter an integer(the input ends if it's 0: "))
print("The sum is", sum)