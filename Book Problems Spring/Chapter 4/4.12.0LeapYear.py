# This program will determine if the year entered is a leap year
year = eval(input("Enter a year: "))

# Check if year is leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)

# Display result
print(year, "is a leap year?", isLeapYear)