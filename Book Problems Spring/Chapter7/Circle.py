# This shows how to define/create a class (classroom)
# class ClassName: ***Naming style: MountainCase***
#   initializer
#   methods
import math

class Circle:
    # Construct a circle object. Constructor format: ClassName(arguments)
    def __init__(self, radius = 1): # data field, constructs a circle
        self.radius = radius        # object of radius 1

    def getPerimeter(self):         # Methods: to get the perimeter
        return 2 * math.pi * self.radius # it needs to be invoked
                                  # then in returns to formula to
    def getArea(self):            # get it. They all have: self
        return math.pi * self.radius ** 2

    def setRadius(self, radius):
        self.radius = radius