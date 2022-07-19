# The code from the previous section is very similar
# the only thing that seems to change is the range of numbers

# It would be nice to write commonly used code once and then be
# able to reuse it
# We can do this by defining a function which allows
# us to to reuse reusable code:

# Define a function and you can give it any name you want
# Lets call this function sum, and dictate its actions,
# (essentially  you tell it what to do)
# Think about this as your base for the reusable code
# This is the code that you would have had to repeat multiple times
def sum(i1, i2):
    result = 0 # sum = 0 initially
    for i in range(i1, i2 + 1): # same as before
        result += i # update sum

    return result # a return keyword is needed to return a result

# Defines a main function that invokes the function sum from above
# This program calls the function and is called a "caller"
# This plugs in stuff
def main():
    print("Sum from 1 to 10 is", sum(1, 10))
    print("Sum from 20 to 37 is", sum(20, 37))
    print("Sum from 35 to 50 is", sum(35, 50))

main() # call the main function