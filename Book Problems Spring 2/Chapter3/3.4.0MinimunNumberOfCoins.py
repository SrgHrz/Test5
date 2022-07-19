# Receive amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount into cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickles in remaining amount
numberOfNickles = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in remaining amount
numberOfPennies = remainingAmount

print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickles, "nickels\n",
      "\t", numberOfPennies, "pennies")