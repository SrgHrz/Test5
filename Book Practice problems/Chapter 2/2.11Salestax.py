# prompt the user for input
purchaseAmount = eval(input("Enter purchase amount: "))

# compute sales tax
tax = purchaseAmount * 0.06 # could have named a constant here: TAX = 0.06

# Display tax amount with two digits after decimal point
print("Sales tax is", int(tax * 100) / 100.0)