# Write a program that reads in a monthly saving amount
# and a number of months and then displays the value of
# a savings account that earns 2% monthly interest after
# the given number of months. For example, suppose the monthly
# saving amount is $100 and the number of months is 3.
# After the first month, the value in the account becomes:
# 100 * (1 + 0.02) = 102.00
# After the second month, the value in the account becomes:
# (100 + 102.00) * (1 + 0.02) = 206.04
# Finally, after the third month the value in the account becomes:
# (100 + 206.04) * (1 + 0.02) = 312.16

# Input Format
# The first line of input will contain the monthly saving
# amount (a non-negative floating point value), and the
# second line of input will contain the number of months
# (a positive integer).

savings = float(input("Enter savings amount: "))
months = int(input("Enter the number of months: "))
accountValue = 0
for i in range(1, months + 1):
    accountValue = (savings + accountValue) * (1.02)
print("account value after", months, "months", "is $", format(accountValue, ".2f"), sep='')

# HR code:
savings = float(input())
months = int(input())
accountValue = 0
for i in range(1, months + 1):
    accountValue = (savings + accountValue) * (1.02)
print("$", format(accountValue, ".2f"), sep='')