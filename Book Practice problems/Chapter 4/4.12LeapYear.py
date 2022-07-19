year = eval(input("Enter a year: ")) # promp user to enter a year

# check if year is leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)

# Display result
print(year, "is a leap year?", isLeapYear) # is leap year = true
print("x is", isLeapYear)