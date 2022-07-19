# Write an if statement that increases pay by 3% if score is
# greater than 90, otherwise it increases pay by 1%
score = eval(input("Enter your score: "))
pay = eval(input("Enter your pay: "))

if score > 90:
    threePayIncrease = pay * 0.03
    newThreePay = pay + threePayIncrease
    print("Your pay has increased by 3% and is now: $" + format(newThreePay, ".2f"))

else:
    onePayIncrease = pay * 0.01
    oneNewPay = pay + onePayIncrease
    print("Your pay has increased by 1% and now is: $" + format(oneNewPay, ".2f"))