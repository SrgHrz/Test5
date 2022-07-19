# convert the following into a for loop

sum = 0
for i in range(1001):
    sum = sum + i

print(sum)
# if you print the sum while nested inside "if" then all the sums up to
# the last one will be printed

# if you print the sum outside if the "if" statement like we have
# here then only the final sum will be printed

print()
print("hello")

i = 1
sum = 0
while i <= 1000:
    sum = sum + i
    i += 1

print(sum)