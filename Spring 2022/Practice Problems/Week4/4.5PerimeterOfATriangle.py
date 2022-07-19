# Write a program that reads the lengths of the three
# edges of a triangle and computes the perimeter if the
# input is valid. Otherwise, display that the input is
# invalid. The input is valid if the sum of every pair
# of two edges is greater than the remaining edge.

# The first line will contain the length of the first edge,
# the second line will contain the length of the second edge,
# and the third line will contain the length of the third edge.
# All edge lengths will be integer values.

edge1 = eval(input("Enter length of edge1: "))
edge2 = eval(input("Enter length of edge2: "))
edge3 = eval(input("Enter length of edge3: "))

if (edge1 + edge2 > edge3) and (edge2 + edge3 > edge1) and (edge3 + edge1 > edge2):
    perimeter = edge1 + edge2 + edge3
    print("The perimeter is", perimeter)
else:
    print("The input is invalid")

# HR code

edge1 = eval(input())
edge2 = eval(input())
edge3 = eval(input())

if (edge1 + edge2 > edge3) and (edge2 + edge3 > edge1) and (edge3 + edge1 > edge2):
    perimeter = edge1 + edge2 + edge3
    print("The perimeter is", perimeter)
else:
    print("The input is invalid")