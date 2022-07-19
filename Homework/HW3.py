# File: Payroll.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique number: 50700
#
# Date Created: 9/18/2020
# Date las modified: 9/18/2020
# Description of program: To create a program that creates a payroll from the input values
# prompt the user for inputs
name = (input("Enter employe's name: "))
hoursWorked = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
fTaxWitholding = eval(input("Enter federal tax witholding rate: "))
sTaxWtholding = eval(input("Enter state tax witholding rate" ))
# calculation
grossPay = hoursWorked * payRate
federalWitholding = fTaxWitholding * grossPay
stateWitholding = sTaxWtholding * grossPay
# Display results
print("")
print("Employe's Name:", name)
print("Hours Worked:", format(hoursWorked,".2f"))
print("Pay Rate:$", format(payRate, ".2f"))
print("Gross Pay:$", grossPay)
print("Deductions:")
print("  Federal Witholding (20%):$", format(federalWitholding, ".2f"))
print("  State Witholding (9.0%):$", format(stateWitholding, ".2f"))
totalDeductions = federalWitholding + stateWitholding
print("  Total Deduction:$", format(totalDeductions, ".2f"))
netPay = grossPay - totalDeductions
print("Net Pay:$", format(netPay, ".2f"))