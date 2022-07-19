import time

currentTime = time.time() # Get current time with a precision of millseconds Ex: 1.123 sec

# obtain total seconds (as an integer because it will give you milliseconds) since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# get current seconds (gets remainder of seconds from the total # of seconds when we divide by 60:minutes)
currentSecond = totalSeconds % 60

# obtain total # of minutes from total seconds (// means as a whole number)
totalMinutes = totalSeconds // 60

# compute the current time in the hour (gets the remaining minutes that didn't make in into groups of 60: hour)
currentMinute = totalMinutes % 60

# obtain total hours as an integer
totalHours = totalMinutes // 60

# compute the current hour (gets the remaining hours after splitting into groups of 24: days)
currentHour = totalHours % 24

# Display results
print("Current time is", currentHour, ":", currentMinute,":", currentSecond)