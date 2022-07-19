# Write a program that reads in a three-digit integer and
# determines whether it is a palindrome number.
# A number is a palindrome number if it reads the same
# from right to left and left to right. EX: 121

number = eval(input("Enter number: "))

digit1 = number % 10 # Results in remainder of 1
digit20 = number // 10 # results in 12 from 121
digit2 = digit20 % 10 # results in remainder of 2 for 12
digit3 = digit20 // 10 # results in 1 from 12

print(digit1, digit2, digit3)

if digit1 == digit3:
    print("YES")
else:
    print("NO")

#HR code

number = eval(input())

digit1 = number % 10 # Results in remainder of 1
digit20 = number // 10 # results in 12 from 121
digit2 = digit20 % 10 # results in remainder of 2 for 12
digit3 = digit20 // 10 # results in 1 from 12


if digit1 == digit3:
    print("YES")
else:
    print("NO")

