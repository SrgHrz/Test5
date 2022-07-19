# print the grade for a score my way
# you can define functions in any order so long as the are before when a function is called
def main():
    score = eval(input("Enter a score: "))

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
    print("The grade is", getGrade(score))




