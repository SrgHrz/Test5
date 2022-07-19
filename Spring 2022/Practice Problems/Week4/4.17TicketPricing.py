# Ticket pricing at the movie theater is as follows:
#
# Regular tickets are 15.
# Tickets for senior citizens (age 65+) are 10. ####
# Tickets for children (under age 10) are 10.
# Mondays are “senior citizen discount days”,  ####
# so their tickets are only 7.
# Thursdays are “children and senior citizen discount days”,   ####
# so children get in for 5 and senior citizens get in for 7.
# Write a program that reads in the day of the week and a
# person's age and prints out the price of their movie ticket.

dayOfWeek = input("Enter the day of the week: ")
age = int(input("Enter person's age: "))

if age < 10:  # Children
    if dayOfWeek == "Thursday":
        print("$5")
    else:
        print("$10")
elif age > 65:  # Seniors
    if dayOfWeek == 'Monday':
        print("$7")
    elif dayOfWeek == 'Thursday':
        print("$7")
    else:
        print("$10")
else:  # Everybody else
    print("$15")

# HR code

dayOfWeek = input()
age = int(input())

if age < 10:  # Children
    if dayOfWeek == "Thursday":
        print("$5")
    else:
        print("$10")
elif age > 65:  # Seniors
    if dayOfWeek == 'Monday':
        print("$7")
    elif dayOfWeek == 'Thursday':
        print("$7")
    else:
        print("$10")
else:  # Everybody else
    print("$15")

