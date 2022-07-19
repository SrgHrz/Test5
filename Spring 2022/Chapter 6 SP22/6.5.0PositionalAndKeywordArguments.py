# a function's arguments can be passes as positional arguments
# or keyword arguments

# Recall the structure when defining a function:
# def functionName(list of parameters): # Function Header
    # Function body

# When calling a function you need to pass arguments to parameters
# There are two kinds of functions: positional (order matters) and
# keyword (order doesn't matter because you are labeling)

# POSITIONAL ARGUMENTS
# Using positional arguments requires that the arguments be passed in
# the same order as indicated by the parameter in the function header

# EX, The following function prints n 3 times:

def nPrintln(message, n):
    for i in range(n):
        print(message)

# We can use: nPrintln('a', 3) to print 'a' 3 times, here 'a' is passed
# on to message because it comes first and 3 is passed onto n because it
# comes next, doing nPrintln(3, n) is incorrect
# Essentially the arguments  must match the parameters in
# order, number and type as defined by the function header

#KEYWORD ARGUMENTS
# We can also pass a function using keyword arguments by labeling them
# in the form of name = value, for example we can do:
# nPrintln(n = 5, message = "good"), in this case the
# arguments can appear in any order

# MIXING
# It is possible to mix the two, just know that positional arguments
# can't appear after keyword arguments, if you're going to use them
# they must appear first

# Ex suppose we have:
# def f (p1, p2, p3):

# We can invoke the function by doing:
# f(30, p2 = 4, p3 = 10)
# which is:
# f(positional, keyword, keyword)
# this is a valid way to invoke
# A wrong way to invoke would be:
# f(30, p2 = 4, 10)
# because the structure is:
# f(positional, keyword, positional)
# because positional arguments can't appear after keyword arguments