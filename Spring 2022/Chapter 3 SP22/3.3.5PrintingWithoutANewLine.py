# Each time one uses a print statement, the output is just on one line
# However sometimes you just might have too much to put on one line
# that you need to carry it over to the next because it might not fit
# just like this comment

# This results in print statements in two different line
print("Hello")
print("World")

# This results in the print statements being in the same line,
# all one needs to use is the escape sequence: end = ' '
print("Hello", end = '')  # Make sure to include a space in the ''
print("World")            # Here we will not

print("Hello", end = ' ')
print("World")
