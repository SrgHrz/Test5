# Prompt the user to enter a radius:
# better to use either: int(input()) to input an integer or...
# to use float(input()) to enter a float (decimal value)
# because eval has security issues...
radius = eval(input("Enter a value for the radius: "))

# Compute the area
area = radius * radius * 3.14159

# Display the result
print("The area for the circle of radius,", radius, "is", area)
