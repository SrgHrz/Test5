# A supermarket awards coupons depending on how much a
# customer spends on groceries. Write a program that reads in
# the amount spent on groceries and prints how much the shopper
# earned as a coupon according to the following rates:
#
# Less than 10 spent - no coupon
# Between 10 and 59.99 spent - 8% coupon
# Between 60 and 149.99 spent - 10% coupon
# Between 150 and 209.99 spent - 12% coupon
# At least 210 spent - 14% coupon
# For example, if the shopper spent 50, they would get a coupon
# worth 8% of that amount, so the program would print out 4.00.

spent = float(input("Enter the amount of money that the shopper spent: "))

if spent < 10:
    print("$0.00")
elif spent <= 59.99:
    coupon = spent * 0.08
    print("$", format(coupon, ".2f"), sep = '')
elif spent <= 149.99:
    coupon = spent * .1
    print("$", format(coupon, ".2f"), sep = '')
elif spent <= 209.99:
    coupon = spent * .12
    print("$", format(coupon, ".2f"), sep = '')
else:
    coupon = spent * .14
    print("$", format(coupon, ".2f"), sep = '')

# HR code
spent = float(input())

if spent < 10:
    print("$0.00")
elif spent <= 59.99:
    coupon = spent * 0.08
    print("$", format(coupon, ".2f"), sep = '')
elif spent <= 149.99:
    coupon = spent * .1
    print("$", format(coupon, ".2f"), sep = '')
elif spent <= 209.99:
    coupon = spent * .12
    print("$", format(coupon, ".2f"), sep = '')
else:
    coupon = spent * .14
    print("$", format(coupon, ".2f"), sep = '')