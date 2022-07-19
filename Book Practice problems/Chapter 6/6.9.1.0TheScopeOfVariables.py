# This program show the difference between local and global variables
globalVar = 1 # This is a global variable and it's accessible to all
def f1(): # Define a function as to perform the commands:
    localVar = 2
    print(globalVar) # Prints global variable b/c a Global variable crated outside of all functions is accesible to all
    print(localVar)

f1() # 1: Tells python to execute this function
print(globalVar) # This variable is global so it works
print(localVar)  # This variable is locally defined so it does not work
