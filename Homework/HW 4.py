# File: DaysInMonth.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique number: 50700
#
# Date Created: 9/25/2020
# Date last modified: 9/25/2020
# Description of program: To create a program that displays the numbers of days from a given month

# Prompt user to enter month and year
monthNumber = eval(input("Enter month as a number that is between 1 and 12 (Ex:Jan = 1) : "))
year = eval(input("Enter the year as 4 integers: "))

# assign group of months: (x,y), to number of days
# 30 days
x = str(30) # corresponds to April, June, September and November
# 31 days
y = str(31) # corresponds to January, March, May, July, August, October, and December



# Assign a month to the number entered
month = monthNumber
if month == 1:
    print("January", year, "has",y, "days")
elif month == 2:
    print("February", year, "has 28 days")
elif month == 3:
    print("March", year, "has",y, "days")
elif month == 4:
    print("April", year, "has",x, "days")
elif month == 5:
    print("May", year, "has",y, "days")
elif month == 6:
    print("June", year, "has",x, "days")
elif month == 7:
    print("July", year, "has",y, "days")
elif month == 8:
    print("August", year, "has",y, "days")
elif month == 9:
    print("September", year, "has",x, "days")
elif month == 10:
    print("October", year, "has",y, "days")
elif month == 11:
    print("November", year, "has",x, "days")
elif month == 12:
    print("December", year, "has",y, "days")
