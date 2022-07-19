# A triangle can be classified based on the lengths of
# its sides. An equilateral triangle has three sides that
# are all the same length. An isosceles triangle has two
# sides that are the same length, and a third side that is
# a different length. If all of the sides have different
# lengths, the triangle is scalene. Write a program that
# reads in the lengths of the three sides of a triangle
# and displays what type of triangle it is.

# The first line of input will contain the length of
# the first side, the second line of input will contain
# the length of the second side, and the thrid line
# of input will contain the length of the thrid side.
# All three side lengths will be positive integers.

side1 = eval(input("Enter length of side1: "))
side2 = eval(input("Enter length of side2: "))
side3 = eval(input("Enter length of side3: "))

if side1 == side2 == side3:
    print("equilateral")
elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print("isosceles")
else:
    print("scalene")

# HR code

side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

if side1 == side2 == side3:
    print("equilateral")
elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print("isosceles")
else:
    print("scalene")