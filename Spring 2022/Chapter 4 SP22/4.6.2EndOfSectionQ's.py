# In this case both statements are printed (if the number is
# even) because the second one will print regardless,
# it is not nested inside the if nest


number = eval(input("Enter a value for the number: "))

if number % 2 == 0:
    print(number, "is even")

print(number, "is odd")