def function(x): # 2: This is activated
    print(x) # 3: Prints global variable b/c local hasn't been define yet
    x = 4.5 # Local variable
    y = 3.4 # Local variable
    print(y) # 4: Prints local variable

x = 2 # Global variable
y = 4 # Global variable
function(x) # 1: This activates the function (x)
print(x) # 5: Prints global variable
print(y) # 6: Prints global variable