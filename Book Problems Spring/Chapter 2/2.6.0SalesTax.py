# Prompt the user for input
purchaseAmount = eval(input("Enter a purchase amount: "))
# Compute sales tax
tax = purchaseAmount * 0.06
# Display tax amount with two digits after the decimal point
print("Sales tax is", int(tax * 100) / 100.0)