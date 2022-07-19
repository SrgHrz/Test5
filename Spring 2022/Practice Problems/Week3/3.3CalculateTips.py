# Write a program that reads the subtotal and the
# gratuity (tip) rate and computes the gratuity and
# total. For example, if the user enters 10 for the subtotal
# and 15% for the gratuity rate, the program displays 1.50
# as the gratuity and 11.50 as the total.

subtotal = eval(input("Please enter a value for the subtotal: "))
gratuity = eval(input("PLease enter a value for the gratuity as a percentage: "))

percentageConversion = gratuity / 100
tip = subtotal * percentageConversion
total = subtotal + tip


print("Tip: $", format(tip, ".2f"), sep="")
print("Total: $", format(total, ".2f"), sep="")

# HR code

subtotal = eval(input())
gratuity = eval(input())

percentageConversion = gratuity / 100
tip = subtotal * percentageConversion
total = subtotal + tip

print("$", format(tip, ".2f"), sep="")
print("$", format(total, ".2f"), sep="")


