# File: EasterSunday.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
#
# Date: 2/06/22
# Description of Program: The purpose of this program is to properly
# use an algorithm that will figure out when Easter Sunday will fall on

# Ask user for input
y = int( input("Enter year: "))
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
r = ( 2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

print("In", y, "Easter Sunday is on month", n, "and day", p)
