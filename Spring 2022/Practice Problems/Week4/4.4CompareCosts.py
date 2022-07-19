# Suppose you shop for rice and find it in two
# different-sized packages. Write a program the reads in
# the the weight and price of each package and then displays
# which one has the better price (measured in cost per unit
# of weight). You can assume the packages won't have the
# same cost per unit of weight.

# The first line will have the weight for package one,
# the second line will have the price for package one,
# the third line will have the weight for package two,
# and the fourth line will have the price for package two.
# All inputs should be treated as floating-point values.

w1 = eval(input("Enter weight for package 1: "))
p1 = eval(input("Enter price for package 1: "))
w2 = eval(input("Enter weight for package 2: "))
p2 = eval(input("Enter price for package 2: "))

costPerWeight1 = p1 / w1
costPerWeight2 = p2 / w2

if costPerWeight1 < costPerWeight2:
    print(1)
else:
    print(2)

#HR code

w1 = eval(input())
p1 = eval(input())
w2 = eval(input())
p2 = eval(input())

costPerWeight1 = p1 / w1
costPerWeight2 = p2 / w2

if costPerWeight1 < costPerWeight2:
    print(1)
else:
    print(2)