# Receive amount
amount = eval(input("Enter the amount, for example, 11.56: "))

# Convert the amount into cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100 # maybe 99c left

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25 # maybe 24c left

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10 # maybe 9c left

# Find the number of nickles in the remaining amount
numberOfNickles = remainingAmount // 5
remainingAmount = remainingAmount % 5 #maybe 4c left

# Find the number pennies left
numberOfPennies = remainingAmount

# Display the result
print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickles, "nickles\n",
      "\t", numberOfPennies, "pennies")