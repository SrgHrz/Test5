# Suppose that tuition for a university is 10,000 this
# year and increases 5% every year. Write a program
# that reads in a non-negative integer and prints out
# the total cost of four years of tuition starting that
# many years from now. For example, if the input is 3,
# we should print out the total cost of tuition over
# years three, four, five, and six, which comes out to 49895.08.

integer = eval(input("Enter an integer: "))
tuition = 10000  # Starting tuition
sum = 0
for year in range(integer, integer + 4):  # span of 4 years (3-6 in ex)
    sum = (tuition * (1.05 ** year)) + sum  # problem: integer doesnt change (year does cycle!!!)
    #print("year is", year)
    #print("sum is", sum)
    #print()
print("Tuition from years", integer, "through", integer + 3, "is", end='')
print(" $", format(sum, ".2f"), sep='')

print()

# HR code
integer = eval(input())
tuition = 10000  # Starting tuition
sum = 0
for year in range(integer, integer + 4):  # span of 4 years (3-6 in ex)
    sum = (tuition * (1.05 ** year)) + sum  # problem: integer doesnt change (year does cycle!!!)
print("$", format(sum, ".2f"), sep='')



