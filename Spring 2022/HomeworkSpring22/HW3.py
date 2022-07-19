# File: Payroll.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
#
# Date: 2/12/22
# Description of Program: This program takes information from the
# user and prints a payroll statement

# User inputs
name = input("Enter employee's name: ")
hoursWorked = eval(input("Enter number of hours worked in a week: "))
hourlyPayRate = eval(input("Enter hourly pay rate: "))
federalTaxWithholdingRate = eval(input("Enter federal tax withholding rate: "))
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate: "))

# Calculations
grossPay = hoursWorked * hourlyPayRate
federalWithholding = grossPay * federalTaxWithholdingRate
stateWithholding = grossPay * stateTaxWithholdingRate
totalDeduction = stateWithholding + federalWithholding
netPay = grossPay - totalDeduction

print("")
print("Employee Name:", name)
print("Hours Worked", format(hoursWorked, ".1f"))
print("Pay Rate: $", format(hourlyPayRate, ".2f"), sep="")
print("Gross Pay: $", format(grossPay, ".2f"), sep="")
print("Deductions:")
print("  Federal Withholding (", format(federalTaxWithholdingRate, ".1%"), sep="", end="")
print(")", sep="", end="")
print(": $", format(federalWithholding, ".2f"), sep="")
print("  State Withholding (", format(stateTaxWithholdingRate, ".1%"), sep="", end="")
print(")", sep="", end="")
print(": $", format(stateWithholding, ".2f"), sep="")
print("  Total Deduction: $", format(totalDeduction, ".2f"), sep="")
print("Net Pay: $", format(netPay, ".2f"), sep="")
