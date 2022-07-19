# Show the error in the following code
print("b")

count = 0
while count < 100:
    print(count)
    count -= 1
# The problem with this loop os that it is an infinite loop that
# continues because subtracting 1 from 0 and so
# on will always be less than 100