# prompt user for input
seconds = eval(input("Enter an integer for seconds: "))

# Gets minutes and remaining seconds
minutes = seconds // 60 # finds minutes from the number of seconds
remainingSeconds = seconds % 60 # seconds reamaining (500/60 --> 8 with 20 as remainder
# finds the left over seconds that didn't make it into groups of 60
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")