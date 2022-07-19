# This section asks which of the following loops are repeated

print("section c")
i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1
# This program is executed an runs well because even though the if
# statement fails we know that it is able to
# move on to the next statement because it is nested in the
# "if" statement.
# Compared to the other previous problems, the remaining instruction
# were still nested inside the "if" statement

# This program essentially prints all the even values