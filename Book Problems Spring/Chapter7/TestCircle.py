from Circle import Circle
# Errors because the circle is a file, it's not a variable created here
def main():

    circle1 = Circle() # Automatically defaults to a radius of 1
    print("The area of the circle of radius",
          circle1.radius, "is", circle1.getArea())
          # access objects data field  #invoke method
          # in this case: radius       # in this case: formula for area defined in Circle file
          # objectRefVar.datafield     #objectRefVar.method(args)
    # Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius",
          circle2.radius, "is", circle2.getArea())
    # Create a circle of radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius",
          circle3.radius, "is", circle3.getArea())
    # Modify circle radius
    circle2.radius = 100 # of circle2.setRadius(100)
    print("The area of the circle of radius",
          circle2.radius, "is", circle2.getArea())
main()