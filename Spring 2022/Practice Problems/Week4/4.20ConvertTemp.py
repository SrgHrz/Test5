# Write a program that converts Fahrenheit to Celsius and
# vice-versa. The conversion equation to convert from
# Fahrenheit to Celsius is:  and the conversion equation
# to convert from Celsius to Fahrenheit is: . Your program
# should read in which unit to start with (F or C) and
# read in the temperature. It should then display the converted
# temperature.

start = input("Input starting unit: ")
temp = float(input("Enter temperature: "))

if start == 'F':
    celsius = (5 / 9) * (temp - 32)
    print(format(celsius, ".1f"))
elif start == 'C':
    fahrenheit = (9 / 5) * (temp) + 32
    print(format(fahrenheit, ".1f"))

# HR code
start = input()
temp = float(input())

if start == 'F':
    celsius = (5 / 9) * (temp - 32)
    print(format(celsius, ".1f"))
elif start == 'C':
    fahrenheit = (9 / 5) * (temp) + 32
    print(format(fahrenheit, ".1f"))