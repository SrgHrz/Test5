# Lets take a structural look at a function

# A function definition consists of the function's name
# (that you choose), parameters , a body
# The syntax of a function is as follows:

# def functionName(list of parameters):
    # Function body

# Some functions return a value: "value returning function"
# a value returning function uses a keyword: "return" which is required
# to return a result
# while others don't and just perform desired operations

# Example code, not fully completed
def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result

def main():
    z = max(1, 2)
    print("The max of the two numbers is", z)

main ()
