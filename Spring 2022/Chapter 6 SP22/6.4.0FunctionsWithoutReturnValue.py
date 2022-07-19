# As we know a function does not have to return a value
# Lets see an example if this:
# This program defines a function named printGrade and invokes it
# to print the grade for a given score

# Print grade for the score
def printGrade(score): # define your base function
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')

def main(): # define your caller
    score = eval(input("Enter a score: "))
    print("The grade is", end = " ")
    printGrade(score) # this does not return any value
                      # thus it is invoked as a statement
main() # Call the main fucntion

# The "printGrade" function does not return any value
# its invoked as a statement in line 22