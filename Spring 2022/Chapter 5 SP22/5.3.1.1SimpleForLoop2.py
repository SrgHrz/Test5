# This gives insight into what does what
integer = eval(input("Enter an integer: "))
sum = 0
for i in range(integer, integer + 4):  # It appears that i is the only value that cycles automatically
    print("i is", i)
    sum = i + sum  # sum changes because we tell it to
    print("integer is:", integer)  # Integer doesnt change
    print("sum is", sum)
    print()