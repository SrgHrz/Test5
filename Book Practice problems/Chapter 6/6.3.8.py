# Find and correct the errors
def function2(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1

def function1(n, m):
    function2(3.4)

function1(2, 3)