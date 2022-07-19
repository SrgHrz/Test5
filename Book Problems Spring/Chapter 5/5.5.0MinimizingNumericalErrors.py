# Initialize sum
sum = 0

# Add 0.01 + 0.02 + 0.03 + ...+ 0.99, 1 to sum
i = 0.01
while i <= 1.0:
    sum += i     # sum = sum + i (sum 
    i = i + 0.01

# Display results
print("the sum is", sum)
# should be 50.5