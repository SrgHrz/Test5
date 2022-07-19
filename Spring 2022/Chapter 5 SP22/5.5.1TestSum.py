# Initialize sum ( add series from .01 to 1.0 incrementing by .01)
sum = 0

# Add 0.01, 0.02, ..., 0.99, 1 to sum
i = 0.01
while i <= 1.0:
    sum += i # you're adding the next value of i
    i = i + 0.01 # you're changing the value of i

# Display result
print("The sum is", sum)
print()
# The correct answer should be 50.5
# When the loop ends, the value of i is slightly larger than 1
# (not exactly 1) which causes that last value not to be added to the sum
# The fundamental problem is that floating point numbers are
# represented by approximations
# To fix the problem,use an integer count to make sure that all the
# numbers are added to the sum

# Initialize sum ( add series from .01 to 1.0 incrementing by .01)
sum = 0

# Add 0.01, 0.02, ..., 0.99, 1 to sum
count = 0
i = 0.01
while count < 100:
    sum += i # you're adding the next value of i
    i = i + .01 # you're changing the value of i
    count += 1 # Increase count

# Display result
print("The sum is", sum)
print()

# We can also use a for loop if we would like

# Initialize sum
sum = 0

# Add 0.01, 0.02, ..., 0.99, 1 to sum
i = 0.01
for count in range(100):
    sum += i # you're adding the next value of i
    i = i + 0.01 # you're changing the value of i

# Display the result
print("The sum is", sum)