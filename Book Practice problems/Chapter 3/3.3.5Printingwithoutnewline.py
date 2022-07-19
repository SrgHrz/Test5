# This is correct
print("He said, \"John's program is easy to read\"")

print("AAA", end = ' ')
print("BBB", end = '')
print("CCC", end = '***')
print("DDD", end = '***')
print (".")

#basically
print("testing 1")
print ("testing 2")

print("testing 1", end = '.....')
print("testing 2", end = '.....')

# New example
import math
radius = 3
print("The area is", radius * radius * math.pi, end = ' ')
print("and the perimeter is", 2 * radius) # wrong perimeter is 2 pi r
# which is know as the circumference

# This is pointless you could have done the following example as:
radius = 3
print("The area is", radius ** 2 * math.pi, "and the circumference is", 2 * math.pi * radius)