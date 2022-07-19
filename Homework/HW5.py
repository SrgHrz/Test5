# File: MinMax.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique number: 50700
#
# Date Created: 10/2/2020
# Date las modified: 10/2/2020
# Description of program: The programs asks the user to enter a series of integers until the user enters
# stop. Once that occurs, the program evaluates the minimum and maximum values

number = input("Enter an integer or ' stop ' to end: " )


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
print("The maximum is", max)
print("The minimum is", min)