#  formula, where an gives the amount of rock in kilograms you collect on day n:

# a_n = 1.62n^3 - n

R = eval(input("Enter a value for R in kg: "))

if R <= 0.62:
    print('1')
elif R <= 10.96:
    print('2')
elif R <= 40.74:
    print('3')
elif R <= 99.68:
    print('4')
elif R <= 197.5:
    print('5')
elif R <= 343.92:
    print('6')
