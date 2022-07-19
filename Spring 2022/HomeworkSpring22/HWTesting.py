answer = input("Enter an integer or 'stop' to end: ")
if answer == 'stop':
    print("You didn't enter any numbers")
while answer != 'stop':
    answer = input("Enter an integer or 'stop' to end: ")
    maximum = max(answer)
    minimum = min(answer)
    print("The maximum is", max)
    print("The minimum is", min)