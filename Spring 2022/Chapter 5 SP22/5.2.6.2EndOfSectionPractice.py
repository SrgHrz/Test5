# This section asks which if the following loops are repeated

print("trial for b")
i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
        i += 1
# Once again the code dies off because i is not even
# The error in this code is that "i =+ 1" is nested inside the
# "if" statement