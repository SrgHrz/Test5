# Write a program that reads in a four-digit integer and
# prints out its digits, one per line, starting with the
# right-most digit. (Hint: Use the % operator to extract
# digits, and use the // operator
# to remove the extracted digit. For instance,
# 4932 % 10 = 2 and 4932 // 10 = 93.)
# Display the integer's digits from right to left,
# one digit per line.

integer = eval(input("Enter an 4-digit integer: "))
digit1 = integer % 10 # results in 2 from 4932
digit21 = integer // 10 # results in 493 from 4932
digit2 = digit21 % 10 # results in 3 from 493
digit31 = digit21 // 10 # results in 49 from 493
digit3 = digit31 % 10 # results in 9 from 49
digit4 = digit31 // 10 # results in 4 from 49

print("Digit 1:", digit1)
print("Digit 2:", digit2)
print("Digit 3:", digit3)
print("Digit 4:", digit4)

# HR code

integer = eval(input())
digit1 = integer % 10 # results in 2 from 4932
digit21 = integer // 10 # results in 493 from 4932
digit2 = digit21 % 10 # results in 3 from 493
digit31 = digit21 // 10 # results in 49 from 493
digit3 = digit31 % 10 # results in 9 from 49
digit4 = digit31 // 10 # results in 4 from 49

print(digit1)
print(digit2)
print(digit3)
print(digit4)
