integer = eval(input("Enter an integer: "))
sum = 0
for i in range(integer, integer + 4):
    print("i is", i)
    sum = i + sum
    print("integer is:", integer)
    print("sum is", sum)