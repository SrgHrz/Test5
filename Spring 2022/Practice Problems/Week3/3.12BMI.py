# Body mass index (BMI) is a measure of health based on
# weight. It can be calculated by taking your weight
# in kilograms and dividing it by the square of your height
# in meters. Write a program that reads in a weight in
# pounds and height in inches and displays the BMI.
# Note that one pound is 0.45359237 kilograms and
# one inch is 0.0254 meters.

pounds = eval(input("Enter weight in pounds: "))
inches = eval(input("Enter height in inches: "))

kilograms = pounds * 0.45359237
meters = inches * 0.0254

bmi = kilograms / (meters ** 2)

print("BMI is ", format(bmi, ".1f"))

# HR code

pounds = eval(input())
inches = eval(input())

kilograms = pounds * 0.45359237
meters = inches * 0.0254

bmi = kilograms / (meters ** 2)

print(format(bmi, ".1f"))