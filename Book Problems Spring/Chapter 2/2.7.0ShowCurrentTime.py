import time

currentTime = time.time() # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second (remainder)
currentSecond = totalSeconds % 60

# Obtain the total minutes (total)
totalMinutes = totalSeconds // 60

# Compute the current minute minute in the hour (remainder)
currentMinute = totalMinutes % 60

# Obtain the total hours (total)
totalHours = totalMinutes // 60

# Compute the current hour (remainder)
currentHour = totalHours % 24

#  Display Results
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")