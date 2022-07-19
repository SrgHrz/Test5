# Prompt the user to enter a radius
radius = eval(input("Enter a value for radius: "))

# Compute area
area = radius * radius * 3.14159

# Display results
print("The area for the circle of radius", radius, "is", area)

# For this to work you must enter the value once command is executed on the run
# tab at the bottom.
# Click run parrallel if asked

# OR
import math # allows us to use math.pi = 3.14....
radius = eval(input("Enter a value for the radius:"))
PI = math.pi
area = radius ** 2 * PI
print("The area of a circle with radius", radius, "is", area)