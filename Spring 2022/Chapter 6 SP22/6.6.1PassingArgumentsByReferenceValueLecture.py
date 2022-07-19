# This involves the use of global and local variable which we
# looked at

# We know that there are two kinds of objects in Python
# 1. Mutable: objects that you can change in the program
# ex: tuple, bytes, list, set, dict
# 2. Immutable: objects that you cant change in your program
# ex: int, float, str, bool

# If you pass a reference to a mutable object, it can be changed by
# your function
# If you pass a reference to an immutable object, it can't be changed
# by your function

# Passing reference to an immutable object (won't change)
def increment (x):
    x += 1
    print("Within the call x is:", x)  # 2. x = 4

x = 3
print("Before the call x is:", x)  # 1. x = 3
increment(x)
print("After the call x is:", x)  # 3. x = 3

print()

# Passing reference to a mutable object (will change)
def revList(lst):
    lst.reverse()
    print("Within the call lst is:", lst)  # 2. lst = [3, 2, 1]

lst = [1, 2, 3]
print("Before the call lst is:", lst)  # 1. lst = [1, 2, 3]
revList(lst)
print("After the call lst is:", lst)  # 3. lst = [3, 2, 1]


