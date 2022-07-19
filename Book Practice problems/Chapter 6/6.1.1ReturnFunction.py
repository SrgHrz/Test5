# Challenge: create an addition function by passing 2 numbers and printing out the sum of those 2 number
# Define a function
def Add(num1 , num2): # This function prints whatever is instructed below
    print(num1 + num2)

# This calls our add function
Add(10,15)

# Now I want to use a return statement and show what it does in a function:
# I have this add function but instead of printing it out I want to store this value somewhere:
# Thus I want to call the function returnAdd
def returnAdd(num1 , num2):
    return (num1 + num2)      # Change print to return and add space
# The return allows you to associate the return to a variable: I will be calling it sum
sum = returnAdd(12, 34)

print(sum)
