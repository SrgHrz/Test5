# Write a program that calculates the energy needed to heat
# water from an initial temperature to a final temperature.
# The formula to compute the energy is: Q = M * (t_f - t_i) * 4184
# M: weight (kg)
# t : temperature in celsius
# Q : energy in joules

m = eval(input("Enter the mass of water in kilograms: "))
ti = eval(input("Enter the initial temp: "))
tf = eval(input("Enter the final temp: "))

Q = m * (tf - ti) * 4184

print("The energy needed is", format(Q, ".1f"), "joules")

# HR code

m = eval(input())
ti = eval(input())
tf = eval(input())

Q = m * (tf - ti) * 4184

print(format(Q, ".1f"))