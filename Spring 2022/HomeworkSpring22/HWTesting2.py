answer = input("Enter an integer or 'stop' to end: ")
if answer == 'stop':
    print("You didn't enter any numbers")
else:
    minimum = answer # assigned to the first integer
    maximum = answer # assigned to the first integer
    while answer != 'stop': # from the first stop, helps keep the loop going
        answer = input("Enter an integer or 'stop' to end: ")
        if answer == 'stop':
            break
        else:
            if answer > maximum: # updates max
                maximum = answer
            elif answer < minimum: # updates min
                minimum = answer
    print("Max is", maximum)
    print("Min is", minimum)