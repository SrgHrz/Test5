# Prompt the user to enter two integers:
n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

gcd = 1 # the initial gcd is 1
k = 2 # the next gcd is 2
while k <= n1 and k <= n2:  # checks if both numbers less than the gcd
    if n1 % k == 0 and n2 % k == 0:  # checks if both numbers are divisible by the gcd
        gcd = k
    k += 1

print("The greatest common divisor for", n1, "and", n2, "is", gcd)