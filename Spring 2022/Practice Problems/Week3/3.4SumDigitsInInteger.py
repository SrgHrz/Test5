# Write a program that reads an integer between 0 and 1000
# and adds all the digits in the integer. For example,
# if an integer is 932, the sum of all its digits is 14.
# (Hint: Use the % operator to extract digits, and
# use the // operator to remove the extracted digit.
# For instance, 932 % 10 = 2 and 932 // 10 = 93.)

integer = eval(input("Enter integer: "))
ones = integer % 10 # results in 2
tensAndHundreds = integer // 10 # results in 93
tens = tensAndHundreds % 10 # results in 3
hundreds = tensAndHundreds // 10 # results in 9

total = ones + tens + hundreds

print("Te total of", integer, "is", total)

# HR code
integer = eval(input())

ones = integer % 10 # results in 2
tensAndHundreds = integer // 10 # results in 93
tens = tensAndHundreds % 10 # results in 3
hundreds = tensAndHundreds // 10 # results in 9

total = ones + tens + hundreds

print(total)

