# Enter annual interest as a pecentage eg. 7.25 (%)
anualInterestRate = eval(input("Enter annual interest rate: "))
monthlyInterestRate = anualInterestRate / 1200

# Enter the number of years
numberOfYears = eval(input("Enter the number of years as an integer: "))

# Enter the loan ammount
loanAmount = eval(input("Enter the loan ammount: "))

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate