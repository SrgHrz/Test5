# Write a program that reads the number of minutes
# and displays the number of years and days for
# the minutes. For simplicity, assume a year has
# 365 days. Round down to the nearest day.
# (Hint: consider using the // and % operators)

minutes = eval(input("Enter the number of minutes as an integer: "))
MINUTESINYEAR = 525600
years = minutes // MINUTESINYEAR # Gets the total number of years from minutes
remainingMinutes = minutes % MINUTESINYEAR # gets the leftover minutes (remainder)
MINUTESINDAY = 1440
days = remainingMinutes // MINUTESINDAY # gets days from leftover (remainder minutes)
print("The total number of years is", years, "years")
print("The total number of minutes is", remainingMinutes, "minutes")
print("The total number of days is", days, "days")

# HR code

minutes = eval(input())
MINUTESINYEAR = 525600
years = minutes // MINUTESINYEAR # Gets the total number of years from minutes
remainingMinutes = minutes % MINUTESINYEAR # gets the leftover minutes (remainder)
MINUTESINDAY = 1440
days = remainingMinutes // MINUTESINDAY # gets days from leftover (remainder minutes)

print(minutes, "minutes is approximately", years, "year(s) and", days, "day(s)")
