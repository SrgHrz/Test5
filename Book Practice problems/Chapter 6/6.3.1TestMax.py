# Return the max of two numbers
def max(num1, num2): # In lines 2-8 we are defining a function
    if num1> num2:   # this is similar to defining a variable
        result = num1 # and it is stored
    else:
        result = num2

    return result

def main():  # This fuction read to the memory
    i = 5
    j = 2
    k = max(i, j) # Call the max function. Tells the max defined function from above to execute
    print("The larger number of", i, "and", j, "is", k)

main() # Calls the main function

#Here main is defined after max. In Python, functions can be defined in any order in a
#script file as long as the function is in the memory when it is called. You can also define
#main before max