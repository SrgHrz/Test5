moneyTotal = int(input("Enter the start amount of money: "))

fastFood = 8
nicerLunch = 15
grandma = 0

lunchChoice = 'start'
total = 0
while lunchChoice != 'end':
    lunchChoice = input("Enter lunch choice: ")
    if lunchChoice == 'fast food':
        fastFood = 8
        moneyTotal = moneyTotal - fastFood
    elif lunchChoice == 'nice lunch':
        nicerLunch = 15
        moneyTotal = moneyTotal - nicerLunch
    elif lunchChoice == 'grandma':
        grandma = 0
        moneyTotal = moneyTotal * 2
print("$", moneyTotal, sep = '')