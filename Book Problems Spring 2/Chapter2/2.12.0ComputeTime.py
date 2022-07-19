import time

currentTime = time.time() # Gets the current time

# Obtain the totals seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Get the current minute in the hour
currentMinute = totalMinutes % 60

# Get the total hours
totalHours = totalMinutes // 60

# Get the current hour
currentHour = totalHours % 24

# Display the result
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")