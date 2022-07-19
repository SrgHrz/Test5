number = eval(input("Enter an integer or ' stop ' to end: " ))

if number == "stop":
    print("You didn't enter any numbers")
else:
    max = int(number)
    min = int(number)

    while True:
        number = input("Enter an integer or ' stop ' to end: " )
        if number != "stop":
            if int(number) > max:
                max = int(number)
            if int(number) < min:
                min = int(number)
        elif number == "stop":
            break
print("The maximun is", max)
print("The minimun is", min)