# This program will let us know the day of the week

# Prompt the user to enter the day of the week
# Monday = 1...Sunday = 7

day = eval(input("Enter the day of the week as a number from 1-7: "))

# Now prompt the user to enter the number of days since "today"
numberOfDays = eval(input("Enter the numbers of days since today: "))

solution = (day + numberOfDays) % 7

print("The solution is", solution)