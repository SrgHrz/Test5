tip1 = float(input("Enter tip 1: "))
tip2 = float(input("Enter tip 2: "))
tip3 = float(input("Enter tip 3: "))
tip4 = float(input("Enter tip 4: "))
tip5 = float(input("Enter tip 5: "))

dollarTip = 1.00

if tip1 < 1.00:
    finalTip1 = dollarTip - tip1
elif tip1 > 5.00:
    finalTip1 = 5.00
else:
    finalTip1 = tip1

print("final tip is", finalTip1)