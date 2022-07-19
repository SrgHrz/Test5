number = eval(input("Enter an integer or ' stop ' to end: " ))
max = int(number)
min = int(number)
# while number != stop, -> to other if statements, if it is equal to stop -> print out a specific statement
if number == "stop":
    print("You didn't enter any numbers")
else:
    int(number) > max
    max = int(number)
    print("max is", max)
else:
    int(number) < min
    min = int(number)
    print("min is", min)
