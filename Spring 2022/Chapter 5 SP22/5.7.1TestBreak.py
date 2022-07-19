# One can use the keyword "break" to immediately terminate
# a loop

# Here is an example:
sum = 0
number = 0

while number < 20:
    number += 1 # increasing the number by 1
    sum += number # adding the new number to the sum
    if sum >= 100:
        break

print("The number is", number)
print("The sum is", sum)