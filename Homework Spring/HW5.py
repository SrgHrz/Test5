integer = input("Enter an integer or \'stop\' to end: ")

max = integer
min = integer

stopLoop = 'stop'
if integer == 'stop' :
    print("You didn't enter any numbers")
while integer != 'stop' :
    integer = input("Enter an integer or \'stop\' to end: ")
    if integer > max:
        max = integer
    if integer < min:
        min = integer
print("The maximum is", max)
print("The minimum is", min)