# Prompt the user for input
seconds = eval(input("Enter an integer for seconds:"))
# Get minutes and remaining seconds
minutes = seconds // 60 # The integer value that it spits out is the total # of minutes
remainingSeconds = seconds % 60 # The remainder that it spits out is the number of left over seconds
print(seconds, "seconds is", minutes, "minutes and",remainingSeconds,"seconds")