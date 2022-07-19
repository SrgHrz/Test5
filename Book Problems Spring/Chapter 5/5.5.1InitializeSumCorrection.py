# Initialize sum
sum = 0
# Add 0.01 + 0.02,....0.99, 1 to sum
count = 0
i = 0.01
while count < 100:
    sum += i      # sum = 0 + 0.1, Increase sum
    i = i + 0.01
    count += 1    # Increase count

# Display result
print("The sum is ", sum)