# The year is divided into four seasons: spring, summer, fall,
# and winter. Assume each season starts on the following dates:
# Spring - March 20, Summer - June 21, Fall - September 22,
# Winter - December 21. (The seasons actually start on
# different dates from year to year, but assume the above
# dates for the purpose of this exercise.) Write a program that
# reads in a month and day and prints the season associated
# with that date.

month = input("Enter month: ")
day = int(input("Enter day: "))

# starting with spring
if month == 'March':
    if day < 20:
        print("winter")
    else:
        print("spring")
elif month == 'April':
    print("spring")
elif month == 'May':
    print("spring")
elif month == 'June':  # transition to summer
    if day < 21:
        print("spring")
    else:
        print("summer")
elif month == 'July':
    print("summer")
elif month == 'August':
    print("summer")
elif month == 'September':  # transition to fall
    if day < 22:
        print("summer")
    else:
        print("fall")
elif month == 'October':
    print("fall")
elif month == 'November':
    print("fall")
elif month == 'December':
    if day < 21:
        print("fall")
    else:
        print("winter")
elif month == 'January':
    print("winter")
else:
    print("winter")

# HR code:

# starting with spring
month = input()
day = int(input())

if month == 'March':
    if day < 20:
        print("winter")
    else:
        print("spring")
elif month == 'April':
    print("spring")
elif month == 'May':
    print("spring")
elif month == 'June':  # transition to summer
    if day < 21:
        print("spring")
    else:
        print("summer")
elif month == 'July':
    print("summer")
elif month == 'August':
    print("summer")
elif month == 'September':  # transition to fall
    if day < 22:
        print("summer")
    else:
        print("fall")
elif month == 'October':
    print("fall")
elif month == 'November':
    print("fall")
elif month == 'December':
    if day < 21:
        print("fall")
    else:
        print("winter")
elif month == 'January':
    print("winter")
else:
    print("winter")
