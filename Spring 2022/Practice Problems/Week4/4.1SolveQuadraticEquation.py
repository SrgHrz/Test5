# The two roots of a quadratic equation ax^2 + bc + c
# can be obtained using the following formulas:

# b^2 - 4ac is called the discriminant of the quadratic equation
#  If it is positive, the equation has two real roots.
#  If it is zero, the equation has one root (i.e. r1 = r2).
#  If it is negative, the equation has no real roots.

# Write a program that reads in the values of a, b, and c,
# and displays the result based on the discriminant.
# If the discriminant is non-negative, display the two roots
# and  (even if they're the same root).
# Otherwise, display "The equation has no real roots".
# Roots should be displayed to three decimal places.

import math

a = eval(input("Enter a value for a: "))
b = eval(input("Enter a value for b: "))
c = eval(input("Enter a value for c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    # This equation has two real roots
    r1 = (-b + math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    r2 = (-b - math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    print("The roots are", format(r1, ".4f"), "and", format(r2, ".4f"))
elif discriminant == 0:
    # This discriminant has one real root
    r1 = (-b + math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    print("The roots are", format(r1, ".4f"), "and", format(r1, ".4f"))
else:
    print("The equation had no real roots")

# HR code

import math

a = eval(input())
b = eval(input())
c = eval(input())

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    # This equation has two real roots
    r1 = (-b + math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    r2 = (-b - math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    print("The roots are", format(r1, ".3f"), "and", format(r2, ".3f"))
elif discriminant == 0:
    # This discriminant has one real root
    r1 = (-b + math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    r2 = (-b - math.sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    print("The roots are", format(r1, ".3f"), "and", format(r2, ".3f"))
else:
    print("The equation has no real roots")