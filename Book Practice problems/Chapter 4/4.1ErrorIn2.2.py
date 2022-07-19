# Prompt the user ot enter a radius
radius = eval(input("Enter a value for radius: "))

import math # imports math module

# Compute area with special parameters
if radius < 0:
    print("Incorrect input")
else:
    area = radius ** 2 * math.pi # You can define variable w/in conditions
    print("Area is", area)

# For this to work you must enter the value once command is executed on the run
# tab at the bottom.
# Click run parrallel if asked

# or

# Prompt the user to enter a radius
radius = eval(input("Enter a value for the radius: "))

import math # imports math module to use math fuctions
PI = math.pi
area = PI * radius ** 2 # I like to define my variables form the very beginning but ideally the are defined w/in
#                         condition statements
if radius < 0:
    print("Incorrect input")
else:
    print("The area is", area)