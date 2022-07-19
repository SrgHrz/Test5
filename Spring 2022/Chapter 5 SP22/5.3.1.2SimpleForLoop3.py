integer = eval(input("Enter an integer: "))
sum = 0
for i in range(integer, integer + 4):  # i is the value that cycles
    print("i is", i)
    sum = i + sum  # This changes because we want it to
    print("integer is:", integer)
    print("sum is", sum)