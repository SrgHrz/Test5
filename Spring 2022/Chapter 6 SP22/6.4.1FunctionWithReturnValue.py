# To see the differences between a function that does
# not return a value and a function that does return a value
# lets redesign the "printGrade" function to return a value, well
# call the new function "getGrade"

# Return the grade for the score:
def getGrade(score):
    if score >= 90.0:
        return('A')
    elif score >= 80.0:
        return('B')
    elif score >= 70.0:
        return('C')
    elif score >= 60.0:
        return('D')
    else:
        return('F')

def main(): # define your caller
    score = eval(input("Enter a score: "))
    print("The grade is", getGrade(score))

main() # call the main fucntion