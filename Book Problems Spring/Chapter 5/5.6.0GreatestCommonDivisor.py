# Prompt the use to enter two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

gcd = 1 # Initial gcd
k = 2 # Possible gcd
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k ==0:
        gcd = k # Greatest common divisor is 2
    k += 1 # k = 2 + 1 = 3 is tried next

print("Th greatest common divisor for",
      n1, "and", n2, "is", gcd)