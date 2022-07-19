# Not sure on the functions: look over for full understanding
x = 1 # Global Variable
def increase(): # 2: This function is activated
    global x # 3: binds a local variable in the global scope
    x = x + 1
    print(x) # Displays 2

increase() # 1: This calls (activates) the function defined "increase"
print(x)   # Displays 2

