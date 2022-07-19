# Problem 1
integer = eval(input("Enter an integer: "))

for i in range(1, integer + 1):
    formula = ((3 * i ** 2) - i) / 2
    print( format(formula, ".0f"), end = " ")

