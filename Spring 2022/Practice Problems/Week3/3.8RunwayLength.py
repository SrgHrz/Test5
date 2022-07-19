# Given an airplane’s acceleration  and take-off speed ,
# you can compute the minimum runway length needed for
# an airplane to take off using the following formula:
# length = v^2 / 2a

v = eval(input("Enter the takeoff speed: "))
a = eval(input("Enter the acceleration: "))

length = (v ** 2) / (2 * a)

print("The min runway length is:", format(length, ".3f"))

# HR code

v = eval(input())
a = eval(input())

length = (v ** 2) / (2 * a)

print(format(length, ".3f"))