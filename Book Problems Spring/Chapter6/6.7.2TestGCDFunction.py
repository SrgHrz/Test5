#import GCDFunction
from GCDFunction import gcd # import the gcd function
# There are errors above because those things are not define here,
# one is the name of the file and the other is the function
# Prompt the user to enter two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest common divisor for", n1,
      "and", n2, "is", gcd(n1, n2))