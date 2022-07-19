def main():
    x = 1 # 1 = object
    print("Before the call, x is", x)
    increment(x)
    print("After the call, x is", x)

def increment(n):
    n += 1
    print("\tn inside the function is", n)

main()
# This is n example of passing an argument by reference value
# As you can see by the output the value of x: 1, is passed to
# the parameter n to invoke the increment function (line 4)
# The parameter n is incremented by 1 in the function but, x is
# not changed no matter what x does.