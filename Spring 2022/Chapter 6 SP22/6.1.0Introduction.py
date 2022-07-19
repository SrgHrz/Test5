# Functions can be used to define reusable code and organize
# and simplify code

# suppose that you need to find the sum of the integers from 1 to 10,
# 20 to 37 and 35 to 49.
# Creating a program to add these three sets of numbers will look like:

# Set 1: Sums 1-10
sum = 0
for i in range (1,11):
    sum += i
print(sum)

# Set 2: Sums 20-37
sum = 0
for i in range(20,38):
    sum += i
print(sum)

# Set3: Sums 35-49
sum = 0
for i in range(35,50):
    sum += i
print(sum)