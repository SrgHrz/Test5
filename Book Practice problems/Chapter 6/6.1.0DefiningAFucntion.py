# Defining functions have a bottom-up approach rather than the usual top-down for human thinking
# the are still executed top-down computationally
# Create a program that will print hello world by defining a function
# Define a function
def HelloWorld(): # What this function will do is print whatever is instructed below. Computer: A function is
    print("Hello World") # created and defined, these are the instructions and I'll wait for the instructions to execute

# This calls the function. It tells the computer to execute the function.
HelloWorld()

# Create a function that will print a name by defining a function
# Define a function
def Greeting(name): # What this function will do is print whatever is instructed below
    print("Hi " + name + "!") # This function will print out "Hi" and a name

# This calls the function
Greeting("Sergio") # This also provides a name as requested by the function

# Challenge: create an addition function by passing 2 numbers and printing out the sum of those 2 numbers
# Define a function
def Add(num1 , num2): # This function prints whatever is instructed below
    print(num1 + num2) # This is what will be performed

# This calls our add function
Add(10,15)