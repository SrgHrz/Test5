# How cold is it outside? The temperature alone is not
# enough to provide the answer.
# Other factors including wind speed, relative humidity, and
# sunshine play important roles in determining coldness outside.
# In 2001, the National Weather Service (NWS) implemented the
# new wind-chill temperature to measure the coldness using
# temperature and wind speed. The formula is given as follows:

# t_wc = 35.74 + 0.6215t_a - 35.75v^0.16 + 0.4275t_av^0.16

# t_a: outside temp
# v: wind speed
#t_wc: wind chill temp

ta = eval(input("Enter a value for the outside temp: "))
v = eval(input("Enter a value for the wind speed: "))

twc = 35.74 + (0.6215 * ta) - (35.75 * v ** 0.16) + (0.4275 * ta * v ** 0.16)

print("The wind chill temp is", format(twc, ".1f"))

# HR code:

ta = eval(input())
v = eval(input())

twc = 35.74 + (0.6215 * ta) - (35.75 * v ** 0.16) + (0.4275 * ta * v ** 0.16)

print(format(twc, ".1f"))
