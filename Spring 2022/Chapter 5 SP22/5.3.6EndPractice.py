# Suppose the input is 2,3,4,5,0,
# What is the output of the following code?

# This program allows you to enter 5 number before
# it ends

number = 0
sum = 0

for count in range(5):
    number = eval(input("Enter an integer: "))
    sum += number

print("sum is", sum)
print("count is", count)

