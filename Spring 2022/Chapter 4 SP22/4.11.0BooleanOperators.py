# Logical Operators/ Boolean Operators: not, and, or
# these operate on the boolean values: "True" or "False"
# to create a new boolean value

# not: The "not" operator negates True to False and False to True
# and: The "and" of two boolean values is true iff both operands are true
# or: The "or" of two boolean values is true if at least one of
# the operands is true

# Lets test these out

# Receive an input
number = eval(input("Enter an integer: "))

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and \
        not (number % 2 == 0 and number % 3 == 0):
    print(number, "is divisible by 2 or 3 but not both")