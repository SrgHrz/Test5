# This program intends to print a message several times
def nPrintIn(message, n):
    for i in range(n):
        print(message)
nPrintIn("Hello", 5) # This calls the function
# Or i can also do this
nPrintIn('a', 3)
# or
nPrintIn(n = 5, message = "good") # This is a keyword argument
                                  # the massage can appear in any
                                  # order
