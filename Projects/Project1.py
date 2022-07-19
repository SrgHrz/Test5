# File: Project1.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique Number: 52090
#
# Date Created: 3/22/21
# Date Modified: 3/23/21
# Description of program: The purpose of this program is to
# create a grade report for a student from their grades that
# they input.

# Student name section
name = input("Enter the student's name: ")
print("")

# Homework Section
print("HOMEWORKS:")
homeworkGrade1 = int(input("  Enter HW1 grade: "))
while homeworkGrade1 > 10 or homeworkGrade1 < 0:
    print("  Grade must be in range [0..10]. Try again.")
    homeworkGrade1 = int(input("  Enter HW1 grade: "))

homeworkGrade2 = int(input("  Enter HW2 grade: "))
while homeworkGrade2 > 10 or homeworkGrade2 < 0:
    print("  Grade must be in range [0..10]. Try again.")
    homeworkGrade2 = int(input("  Enter HW2 grade: "))

homeworkGrade3 = int(input("  Enter HW3 grade: "))
while homeworkGrade3 > 10 or homeworkGrade3 < 0:
    print("  Grade must be in range [0..10]. Try again.")
    homeworkGrade3 = int(input("  Enter HW3 grade: "))

print("")

# Project Section
print("PROJECTS:")
projectGrade1 = int(input("  Enter Project1 grade: "))
while projectGrade1 > 100 or projectGrade1 < 0:
    print("  Grade must be in range [0..100]. Try again.")
    projectGrade1 = int(input("  Enter Project1 grade: "))

projectGrade2 = int(input("  Enter Project2 grade: "))
while projectGrade2 > 100 or projectGrade2 < 0:
    print("  Grade must be in range [0..100]. Try again.")
    projectGrade2 = int(input("  Enter Project2 grade: "))

print("")

# Exam Section
print("EXAMS:")
examGrade1 = int(input("  Enter Exam1 grade: "))
while examGrade1 > 100 or examGrade1 < 0:
    print("  Grade must be in range [0..100]. Try again.")
    examGrade1 = int(input("  Enter Exam1 grade: "))

examGrade2 = int(input("  Enter Exam2 grade: "))
while examGrade2 > 100 or examGrade2 < 0:
    print("  Grade must be in range [0..100]. Try again.")
    examGrade2 = int(input("  Enter Exam2 grade: "))

print("")

# Grade Report section
print("Grade report for:", name)
homeworkGradeTotal = (homeworkGrade1 + homeworkGrade2 + homeworkGrade3)
homeworkGradePointsAwarded = (homeworkGradeTotal / 30) * 100
print("  Homework average (30% of grade): ", format(homeworkGradePointsAwarded, ".2f"))

projectGradeTotal = (projectGrade1 + projectGrade2)
projectGradePointsAwarded = (projectGradeTotal / 200) * 100
print("  Project average (30% of grade): ", format(projectGradePointsAwarded, ".2f"))

examGradeTotal = (examGrade1 + examGrade2)
examGradePointsAwarded = (examGradeTotal / 200) * 100
print("  Exam average (40% of grade):", format(examGradePointsAwarded, ".2f"))

studentAverage = format(((homeworkGradePointsAwarded * 0.3) + (projectGradePointsAwarded * 0.3) + (examGradePointsAwarded) * 0.4), ".2f")
print("  Student course average: ", studentAverage)

if studentAverage >= str(90.0):
    print("  Course grade (CS303E : Spring, 2021): A")
elif studentAverage >= str(80.0):
    print("  Course grade (CS303E : Spring, 2021): B")
elif studentAverage >= str(70.0):
    print("  Course grade (CS303E : Spring, 2021): C")
elif studentAverage >= str(60.0):
    print("  Course grade (CS303E : Spring, 2021): D")
else:
    print("  Course grade (CS303E : Spring, 2021): F")
