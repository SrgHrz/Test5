# To format floating point numbers we use:
# width.precisionf
# width: field width, precision: decimal places,
# f: format specifier/ conversion code (sets format for
# floating point numbers

# By default These are all right justified if I include a field width
# Means that python starts to display from the right
# leaving a black spaces on the left
print(format(57.467657, "10.2f"))
print(format(12345678.923, "10.2f"))
print(format(57.4, "10.2f"))
print(format(57, "10.2f"))
print(format(57, ".2f"))
print()

# If you want the number to be left justified all one has
# to do is to use: < in the format specifier
print(format(57.467657, "10.2f"))
print(format(57, "<10.2f"))