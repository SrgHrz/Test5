print("        Multiplication Table")
# Display the number title
print("  |", end = '')
for j in range (1, 10):
    print(" ", j, end = '')
print() # Jump to a new line
print("------------------------------------")

# Display table body
for i in range (1, 10):
    print(i, "|", end = '')
    for j in range (1, 10):
        # Display the product and align properly
        print(format(i * j, "3d"), end = '')
    print() # Jump to a new line

# Here the only thing that I changed was the fact that I
# changed 4d to 3d to get the numbers to all align