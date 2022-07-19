# This program increases the pay by 3% if score is > 90
pay = eval(input("Enter your pay amount: $ "))
score = eval(input("Enter your score: "))
if score > 90:
    payIncrease = pay * 0.03
    newPay = pay + payIncrease
    print("Your new pay is", format(newPay, ".2f"))
else:
    print("Your pay did not increase and it is still: $"+ format(pay, ".2f"))