# A variable created inside a function is referred to as a
# "local variable"
# Local variables can only be accessed within a function
# The scope of a local variable starts from its creation and
# continues to the end of the function that contains the variable

# In Python you can also use "global variables" which are created
# outside all functions and are accessible to all  functions in their scope

# EX 1:
globalVar = 1
def f1():  # fucntion
    localVar = 2
    print(globalVar)  # prints 1
    print(localVar)  # prints 2

f1()  # this calls function1
print(globalVar)  # prints 1
# print(localVar)  # Out of scope, so this gives an error

print()

# EX 2:
x = 1
def f1():  # fucntion
    x = 2
    print(x)  # prints the local variable: 2
              # global variable not accessible inside the function
f1()  # calls function1
print(x)  # prints the global variable: 1

print()

# EX 3:
x = eval(input("Enter a number: "))
if x > 0:
    y = 4

print(y)  # thins gives an error if the value of x is <= 0
          # because the variable y is not created

print()

# EX 4:
sum = 0
for i in range(5):
    sum += 1

print(i)