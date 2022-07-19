purchaseAmount = eval(input("Enter a purchase amount: "))

tax = purchaseAmount * 0.06
salesTax = int(tax * 100) / 100.0

print("Sales tax is", salesTax)