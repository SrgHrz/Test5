# Write a program that reads in an arbitrary number of
# integers and determines how many positive and negative
# values have been read. The value 0 will indicate the end
# of input and should not be counted toward either count.

# Each line of input will contain an integer, and
# the last line of input will contain the value 0.

integer = 1 # Initial value to get the loop started
countPos = 0
countNeg = 0
while integer != 0:
    integer = eval(input("Enter an integer: "))
    if integer > 0:
        countPos = countPos + 1
    elif integer < 0:
        countNeg = countNeg + 1
print("Pos:", countPos, ", Neg:", countNeg)

# HR code

integer = 1 # Initial value to get the loop started
countPos = 0
countNeg = 0
while integer != 0:
    integer = eval(input())
    if integer > 0:
        countPos = countPos + 1
    elif integer < 0:
        countNeg = countNeg + 1
print(countPos, countNeg)

