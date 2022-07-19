# Write an if statement that increases pay by 3% if
# the score is greater than 90

score = eval(input("Enter your score (current pay: $20/h): "))
if score > 90:
    print("Your pay has increased by 3%")
    netPay = 20
    calc = netPay * 0.03
    newPay = netPay + calc
    print("New net pay: $", format(newPay, ".2f"), sep="")