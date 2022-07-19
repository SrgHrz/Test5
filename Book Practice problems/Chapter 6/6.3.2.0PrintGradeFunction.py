# print grade for the score
def getGrade(score): # Define a function that prints whatever is instructed below
    if score >= 90.0:
        return('A')
    elif score >= 80.0:
        return('B')
    elif score >= 70.0:
        return('C')
    elif score >=  60.0:
        return('D')
    else:
        return('F')

def main(): # This also defines a function
    score = eval(input("Enter a score: "))
    print("The grade is", getGrade(score))

main() # This calls the main function from above because the function is called main
       # The fuction then calls the getGrade Function