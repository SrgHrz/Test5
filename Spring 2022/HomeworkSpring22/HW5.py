# File: MinMax.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
#
# Date: 2/27/22
# Description of Program: The purpose of this program is to determine the
# minimum and maximum values from a series of user inputs

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