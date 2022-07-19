number = eval(input("Enter an integer or ' stop ' to end: " ))
max = int(number)
min = int(number)
# while number != stop, -> to other if statements, if it is equal to stop -> print out a specific statement
if number == "stop":
    print("You didn't enter any numbers")

elif number != "stop":
        number = eval(input("enter in integer: "))
        if number > max:
            max = int(number)
        else:
            number < min
            min = int(number)