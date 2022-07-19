# You can use Cramer's rule to solve the following 2x2 system
# of linear equations:

# ax + by = e
# cx + dy = f

# In this case Cramer's rule says:

# x = (e*d - b*f) / (a*d - b*c)
# y = (a*f - e*c) / (a*d - b*c)

# Write a program that reads in the values a, b, c, d, e, and f
# and displays the result. If ad - bc is 0, report that
# "The equation has no solution".
# The values of x and y should be displayed to one decimal place.

a = eval(input("Enter the value for a: "))
b = eval(input("Enter the value for b: "))
c = eval(input("Enter the value for c: "))
d = eval(input("Enter the value for d: "))
e = eval(input("Enter the value for e: "))
f = eval(input("Enter the value for f: "))

denominator = (a * d) - (b * c)

if denominator != 0:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", format(x, ".1f"), "and y is", format(y, ".1f"))
else:
    print("The equation has no solution")

# HR code

a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())
f = eval(input())

denominator = (a * d) - (b * c)

if denominator != 0:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", format(x, ".1f"), "and y is", format(y, ".1f"))
else:
    print("The equation has no solution")
