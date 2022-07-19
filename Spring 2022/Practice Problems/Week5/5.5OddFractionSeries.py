# Write a program that reads in a positive integer n and
# prints out the value of the following series, rounded to
# two decimal places:

# 1/3 + 3/5 + 5/7 + ... 2n-1 / 2n + 1

# The only line of input will contain a single positive integer n.

integer = int(input("Enter an integer: "))
sum = 0
for n in range(integer + 1):
    fraction = ((2 * n) - 1) / ((2 * n) + 1)
    #print(fraction)
    sum = fraction + sum  # new sum is fraction plus the old sum
    #print("sum is", sum)
    #print()
print("sum is", format(sum + 1, ".2f"))  # need to add a +1 due to how range is carried out

# HR code
integer = int(input())
sum = 0
for n in range(integer + 1):
    fraction = ((2 * n) - 1) / ((2 * n) + 1)
    sum = fraction + sum  # new sum is fraction plus the old sum
print(format(sum + 1, ".2f"))  # need to add a +1 due to how range is carried out
