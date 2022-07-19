# Write a program that reads in the radius and
# length of a cylinder and computes the area and
# volume using the following formulas:
# area = pi * r^2
# volume = area * length

radius = eval(input("Enter a value for the radius: "))
length = eval(input("Enter a value for the length: "))
PI = 3.14159

area = PI * radius ** 2
volume = area * length

print("Area:", format(area, ".2f"))
print("Volume", format(volume, ".2f"))

# HR code
radius = eval(input())
length = eval(input())

# need to either use lots of digits for PI of use math.PI to
# get exact value, ti little digits on PI lead to an error
# because the system might put in a very large value for
# the radius
PI = 3.14159265

area = PI * radius ** 2
volume = area * length

print(format(area, ".2f"))
print(format(volume, ".2f"))