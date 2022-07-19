# Write a program that reads in the test scores of five
# students and then prints out the difference between the
# highest and the second-higest scores. Do NOT use lists or the
# sort utility.
# Input Format:
# Each line of input will contain the score of a single
# student, a non-negative integer. There will be a total of
# five lines of input.

score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the second score: "))
score3 = int(input("Enter the third score: "))
score4 = int(input("Enter the fourth score: "))
score5 = int(input("Enter the fifth score: "))

# assumes score 1 is the highest score
if score1 >= score2 and score1 >= score3 and score1 >= score4 and score1 >= score5:
    highest = score1
    # look for second highest (dont use score 1)
    if score2 >= score3 and score2 >= score4 and score2 >= score5:
        secondHighest = score2
    elif score3 >= score2 and score3 >= score4 and score3 >= score5:
        secondHighest = score3
    elif score4 >= score2 and score4 >= score3 and score4 >= score5:
        secondHighest = score4
    else:
        secondHighest = score5
    print(highest - secondHighest)
# assumes second score is the highest
elif score2 >= score1 and score2 >= score3 and score2 >= score4 and score2 >= score5:
    highest = score2
    # look for second highest (dont use score 2)
    if score1 >= score3 and score1 >= score4 and score1 >= score5:
        secondHighest = score1
    elif score3 >= score1 and score3 >= score4 and score3 >= score5:
        secondHighest = score3
    elif score4 >= score1 and score4 >= score3 and score4 >= score5:
        secondHighest = score4
    else:
        secondHighest = score5
    print(highest - secondHighest)
# Assumes that the third scores is the highest
elif score3 >= score1 and score3 >= score2 and score3 >= score4 and score3 >= score5:
    highest = score3
    # look for second highest (dont use score 3)
    if score1 >= score2 and score1 >= score4 and score1 >= score5:
        secondHighest = score1
    elif score2 >= score1 and score2 >= score4 and score2 >= score5:
        secondHighest = score2
    elif score4 >= score1 and score4 >= score2 and score4 >= score5:
        secondHighest = score4
    else:
        secondHighest = score5
    print(highest - secondHighest)
# Assumes that the fourth scores is the highest
elif score4 >= score1 and score4 >= score2 and score4 >= score3 and score4 >= score5:
    highest = score4
    # look for second highest (dont use score 4)
    if score1 >= score2 and score1 >= score3 and score1 >= score5:
        secondHighest = score1
    elif score2 >= score1 and score2 >= score4 and score2 >= score5:
        secondHighest = score2
    elif score3 >= score1 and score3 >= score2 and score3 >= score5:
        secondHighest = score3
    else:
        secondHighest = score5
    print(highest - secondHighest)
# Assumes that the fifth scores is the highest
elif score5 >= score1 and score5 >= score2 and score5 >= score3 and score5 >= score4:
    highest = score5
    # look for second highest (dont use score 5)
    if score1 >= score2 and score1 >= score3 and score1 >= score4:
        secondHighest = score1
    elif score2 >= score1 and score2 >= score3 and score2 >= score4:
        secondHighest = score2
    elif score3 >= score1 and score3 >= score2 and score3 >= score4:
        secondHighest = score3
    else:
        secondHighest = score4
    print(highest - secondHighest)
