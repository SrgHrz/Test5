# File: DaysInMonth.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
#
# Date: 2/19/22
# Description of Program: To display the number of days is a month

# Ask user for input for the year and the month
year = eval(input("Please enter a year: "))
month = eval(input("Please enter a month: "))

# months with 30 days: 9,4,6,11 (4,6,9,11)
# the rest have 31: 1,3,5,7,8,10,12
# february has 28
# on leap year it has 29

if month % 12 == 0:
    print("December", year,"has 31 days")
elif month % 11 == 0:
    print("November", year, "has 30 days")
elif month % 10 == 0:
    print("October", year, "has 31 days")
elif month % 9 == 0:
    print("September", year, "has 30 days")
elif month % 8 == 0:
    print("August", year, "has 31 days")
elif month % 7 == 0:
    print("July", year, "has 31 days")
elif month % 6 == 0:
    print("June", year, "has 30 days")
elif month % 5 == 0:
    print("May", year, "has 31 days")
elif month % 4 == 0:
    print("April", year, "has 30 days")
elif month % 3 == 0:
    print("March", year, "has 31 days")
elif month % 2 == 0:
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
                 (year % 400 == 0)
    if isLeapYear:
        print("February", year, "has 29 days")
    else:
        print("February", year, "has 28 days")
else:
    print("January", year, "has 31 days")
