def main():
    max = 1
    getMax(1, 2, max)
    print(max)

def getMax(value1, value2, max):
    if value1 > value2:
        max = value1
    else:
        max = value2

main()

# This is an example of passing an argument by reference value
