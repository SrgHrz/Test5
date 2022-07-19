# One can use the conversion code s to format a
# string with a specified width
# By fault strings are left justified

print(format("Welcome to Python", "20s"))
print(format("Welcome to Python", "<20s"))
print(format("Welcome to Python", ">20s"))
print(format("Welcome to Python and Java", ">20s"))