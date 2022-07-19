def main(): # 2: This funcction is executed
    x = 1
    print("Before the call, x, is", x) # 3: This is printed
    increment(x)       #4: This variable calls the function below
    print("After the call, x, is", x) # 7: This thing is printed

def increment(n): # 5: This function is called
    n += 1
    print("\tn inside the function is", n) # 6: This is printed

main() # 1: This calls the function
# the purpose of this program is to show that the value of
# x does not change. It only shows that it did increase by one
# but it does not permanently change its value