# Print the grade for the score
# This structure is a bottom-up approach and not the conventional top-down when thinking about constructing
# Lables are placed to indicate thought process
# This is a modified program that prints "Invalid score for invalid scores
def printGrade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return # same as return None

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

def main(): # 2: This function is executed
    score = eval(input("Enter a score: "))
    print("The grade is", printGrade(score)) # 3: the printGrade score defined function is executed from above

main() # 1: This calls the main function from above. The fucntions have be previously defined before their use