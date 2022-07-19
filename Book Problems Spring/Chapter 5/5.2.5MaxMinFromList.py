number = eval(input("Enter an integer: "))
max = number
min = number

while number != 0:
    number = eval(input("Enter an integer: "))
    if number > max:
        max = number
    if number < min:
        min = number
    if number == max == min:
        print("max is", max)
        print("min is", min)

print("max is", max)
print("min is", min)
print("number", number)