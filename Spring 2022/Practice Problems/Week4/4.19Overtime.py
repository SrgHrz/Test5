# Write a program that reads in the hourly wage of an
# employee and how many hours they worked in a given week
# and then prints out the employee's pay for the week. Any
# overtime worked (any time over 40 hours per week) is paid
# at 150% of the regular hourly wage.

wage = float(input("Enter an hourly wage: "))
hours = float(input("Enter the hours worked: "))

if hours <= 40:
    pay = wage * hours
    print("$", format(pay, ".2f"), sep = '')
else:
    pay1 = wage * 40
    pay2 = (wage * 1.5) * (hours - 40)
    netPay = pay1 + pay2
    print("$", format(netPay, ".2f"), sep = '')

# HR code

wage = float(input())
hours = float(input())

if hours <= 40:
    pay = wage * hours
    print("$", format(pay, ".2f"), sep = '')
else:
    pay1 = wage * 40
    pay2 = (wage * 1.5) * (hours - 40)
    netPay = pay1 + pay2
    print("$", format(netPay, ".2f"), sep = '')