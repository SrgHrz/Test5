# Lets say you have something like x = 3....
# Because all data are objects in Python,
# a variable (x) for an object (3, which is an integer, and we know
# that integer is an object) is actually a reference to the object

# When invoking a function with arguments...
# ex: def sum (n1, n2): Here this function has 2 arguments
# which us our parameters
#... We say that the value of the argument is passed to a parameter
# when invoking a function
# If the argument is a number or a string, the argument is not affected
# regardless of the changes made to the parameter inside the function

# Ex:
def main():
    x = 1
    print("Before the call, x is", x)
    increment(x)
    print("After the call, x is", x)

def increment(n):
    n += 1
    print("\tn inside the function is", n)

main()

# The value of x(1) is passed to parameter n to invoke the increment
# function. x = 1 -> Increment function (looks like were changing x)
# -> were actually changing n with n taking up the value of x(1) ->
# n is incremented  to 2 -> the value of x after the increment (nothing
# happened is called)

# Why? numbers and strings are immutable objects and their contents
# (id) cant be changed

# Ex:
# x = 4
# y = x
# Therefore id(x) = id(y) = same id #, the fact that y = x,
# doesnt change the id of x = 4 since 4 is a number and that can't
# change. Recall from earlier that if you have two separate
# variables that point to the same number: x = 1, and y = 1
# then they will have the same id because there is no need to
# generate 2 separate id's if the y are the number