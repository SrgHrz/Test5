# File: Payroll.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique Number: 52090
#
# Date Created: 2/14/21
# Date Modified: 2/14/21
# Description of program: This program takes in input from the user in order to generate a payroll statement

employeesName = (input("Enter employee's name: "))
hoursWorked = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
grossPay = hoursWorked * payRate
federalTaxRate = eval(input("Enter federal tax withholding rate: "))
federalWithholding = grossPay * federalTaxRate
stateTaxRate = eval(input("Enter state tax withholding rate: "))
stateTax = grossPay * stateTaxRate
totalDeduction = federalWithholding + stateTax
netPay = grossPay - (federalWithholding + stateTax)

print("")
print("Employee Name:", employeesName)
print("Hours Worked:", format(hoursWorked, ".1f"))
print("Pay Rate: $" + format(payRate, ".2f"))
print("Gross Pay: $" + format(grossPay, ".2f"))
print("Deductions:")
print("  Federal Withholding (" + format(federalTaxRate, ".1%") + "): $" + format(federalWithholding, ".2f"))
print("  State Withholding (" + format(stateTaxRate,".1%") + "): $" + format(stateTax, ".2f"))
print("  Total Deduction: $" + format(totalDeduction, ".2f"))
print("Net Pay: $" + format(netPay, ".2f"))
