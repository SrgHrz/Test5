sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break      # The break here uis used to terminate a loop

    print("The number is", number)
    print("The sum is", sum)
