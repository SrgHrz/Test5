# This program will obtain the minutes and seconds from the amount of
# time in seconds

seconds = eval(input("Enter an integer in seconds: "))

# Get the remaining minutes and seconds
minutes = seconds // 60 # Obtains the total number of minutes
remainingSeconds = seconds % 60 # Obtains the remaining seconds

# print the result
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")
