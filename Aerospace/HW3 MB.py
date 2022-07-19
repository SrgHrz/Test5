# This program computes the mach numbers and property changes given M1 and beta

import math

# Constant for PI
PI = math.pi

# Ask for user input
m1 = eval(input("Enter a value for m1: "))
beta = eval(input("Enter a value for beta in degrees: "))

# Concerts for degrees to radians
radians = beta * (PI / 180)

# Solving for theta
theta = math.degrees(math.atan((2 * (1 / math.tan(radians))) * ((((m1 ** 2) * (math.sin(radians) ** 2) - 1)) / ((m1 ** 2) * (1.4 + math.cos(2 * radians)) + 2))))

# Solving for Mn1
mn1 = m1 * math.sin(radians)

# Solving for Mn2
mn2 = ((1 + ((1.4 - 1) / 2) * (mn1 ** 2)) / ((1.4 * (mn1 ** 2)) - ((1.4 - 1)) / 2)) ** (1/2)

# Solving for M2
# convert theta to radians:
radians2 = theta * (PI / 180)
m2 = mn2 / math.sin(radians - radians2)

# Solving for rho2/rho1 (density ratio)
densityRatio = ((1.4 + 1) * (mn1 ** 2)) / (2 + (1.4 - 1) * (mn1 ** 2))

# Solving for P2/P1 (pressure ratio)
pressureRatio = 1 + ((2 * 1.4) / (1.4 + 1)) * ((mn1 ** 2) - 1)

# Solving for T2/T1 (temperature ratio)
temperatureRatio = pressureRatio * ((2 + (1.4 - 1) * (mn1 ** 2)) / ((1.4 + 1) * (mn1 ** 2)))

# Solving for stagnation pressure ratio (P02/Po1)
stagnationPressureRatio = pressureRatio * ((1 + ((1.4 - 1) / 2) * (mn2 ** 2)) / (1 + ((1.4 - 1) / 2) * (mn1 ** 2))) ** (1.4 / (1.4 - 1))


# Print solutions:
print()
print("Results:")
print("Theta:", format(theta,".2f"), "degrees")
print("Mn1:", format(mn1, ".2f"))
print("Mn2:", format(mn2, ".2f"))
print("M2:", format(m2, ".2f"))
print("Density Ratio (rho2/rho1):", format(densityRatio, ".2f"))
print("Pressure Ratio (P2/P1):", format(pressureRatio, ".2f"))
print("Temperature Ratio(T2/T1):", format(temperatureRatio, ".2f"))
print("Stagnation Pressure Ratio(Po2/Po1):", format(stagnationPressureRatio, ".2f"))



#test = math.sin(radians)
#test2 = math.sin(radians) ** 2

#print(test, test2)

#part1 = 2 * (1 / math.tan(radians))
#part2 = ((m1 ** 2) * (math.sin(radians) ** 2) - 1)
#part3 = ((m1 ** 2) * (1.4 + math.cos(2 * radians)) + 2)

#print(part1)
#print(part2)
#print(part3)

#thetaTest = math.degrees(math.atan(part1 * (part2/part3)))
#print(thetaTest)
