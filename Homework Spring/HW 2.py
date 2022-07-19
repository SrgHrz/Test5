# File: EasterSunday.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
# Unique Number: 52090
#
# Date Created: 2/7/21
# Date Modified: 2/7/21
# Description of program: The purpose of this program is to use an algorithm along with user import of a year
#                         in order to determine the month and day of Easter Sunday

y = eval(input("Enter year: "))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
print("In", y, "Easter Sunday is on month", n,"and day",p)