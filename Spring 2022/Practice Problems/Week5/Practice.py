max1 = 0
max2 = 0
for i in range(5):
    grade = int(input("Enter a grade "))
    if grade >= max1:  # If the first input > 0: (100), or the current max gets replaced
        max1 = grade  # and max = first value that you input (100), or the new max gets updated
        max2 = max1  # then max 2 = 0, or the former max becomes the second max
    if max2 <= grade < max1:  # for second input(90): 0 <= 90 <= 100
        max2 = grade  # or the second max gets updated
print(max1 - max2)