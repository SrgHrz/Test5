# Formatting in scientific notation is the
# Same thing as formatting integers except that we change
# the conversion code from f to e

print(format(57.467657, "10.2e"))
print(format(57.4, "10.2e"))
print(format(57, "10.2e"))
print()
# Formatting as a percentage is the
# Same thing as formatting integers except that we change
# the conversion code from f to %
# !!! The % sign causes the number to be multiplied by 100 !!!
print(format(57.467657, "10.2%"))
print(format(57.4, "10.2%"))
print(format(57, "10.2%"))
print(format(0.57, "10.2%"))  # Think about it as 57 out of 100