x = eval(input("Enter a integer: "))
y = eval(input("Enter a integer: "))
if x ** y < 10000:
    print(format(x ** y, ".2f"))
else:
    print(format(x / y, ".2f"))