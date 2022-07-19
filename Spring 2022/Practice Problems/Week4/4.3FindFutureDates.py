# Write a program that reads in an integer for today's day
# of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6)
# and reads in a number of days to elapse, and then
# displays the current day of the week, as well as the
# day of the week once the given number of days has elapsed.

day = eval(input("Enter the day of the week as an integer: "))
daysElapsed = eval(input("Enter the number of days elapsed: "))
if day == 0:
    print("Today is Sunday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Sunday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Saturday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Friday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Thursday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Wednesday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Tuesday")
    else:
        print("and the future day is Monday")
elif day == 1:
    print("Today is Monday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Monday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Sunday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Saturday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Friday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Thursday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Wednesday")
    else:
        print("and the future day is Tuesday")
elif day == 2:
    print("Today is Tuesday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Tuesday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Monday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Sunday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Saturday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Friday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Thursday")
    else:
        print("and the future day is Wednesday")
elif day == 3:
    print("Today is Wednesday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Wednesday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Tuesday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Monday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Sunday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Saturday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Friday")
    else:
        print("and the future day is Thursday")
elif day == 4:
    print("Today is Thursday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Thursday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Wednesday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Tuesday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Monday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Sunday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Saturday")
    else:
        print("and the future day is Friday")
elif day == 5:
    print("Today is Friday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Friday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Thursday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Wednesday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Tuesday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Monday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Sunday")
    else:
        print("and the future day is Saturday")
else:
    print("Today is Saturday", end = ' ')
    if daysElapsed % 7 == 0:
        print("and the future day is Saturday")
    elif daysElapsed % 6 == 0:
        print("and the future day is Friday")
    elif daysElapsed % 5 == 0:
        print("and the future day is Thursday")
    elif daysElapsed % 4 == 0:
        print("and the future day is Wednesday")
    elif daysElapsed % 3 == 0:
        print("and the future day is Tuesday")
    elif daysElapsed % 2 == 0:
        print("and the future day is Monday")
    else:
        print("and the future day is Sunday")
