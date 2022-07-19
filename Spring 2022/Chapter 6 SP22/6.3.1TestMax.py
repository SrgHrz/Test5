# Return the max of two numbers
def max(num1, num2): # define your function
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result

def main(): # define your caller
    i = 5
    j = 2
    k = max(i, j) # calls the max function
    print("The larger number of", i, "and", j, "is", k)

main() # calls the main fucntion