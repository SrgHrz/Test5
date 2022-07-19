# File: DaysInMonth.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique Number: 52090
#
# Date Created: 2/25/21
# Date Modified: 2/25/21
# Description of program: This program asks the user for a year and a month
# then it will display how many days the month has

# Ask user for input
year = eval(input("Please enter a year: "))
month = eval(input("Please enter a month: "))

if month == 1:
    print("January", year, "has 31 days")
elif month == 3:
    print("March", year, "has 31 days")
elif month == 4:
    print("April", year, "has 30 days")
elif month == 5:
    print("May", year, "has 31 days")
elif month == 6:
    print("June", year, "has 30 days")
elif month == 7:
    print("July", year, "has 31 days")
elif month == 8:
    print("August", year, "has 31 days")
elif month == 9:
    print("September", year, "has 30 days")
elif month == 10:
    print("October", year, "has 31 days")
elif month == 11:
    print("November", year, "has 30 days")
elif month == 12:
    print("December", year, "has 31 days")
elif month == 2:
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
                 (year % 400 == 0)
    if isLeapYear == 1:
        print("February", year, "has 29 days")
    else:
        print("February", year, "has 28 days")