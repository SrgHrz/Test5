# Example from lecture notes

def sumToN(n):
    # Sum integers from 1 to n
    sum = 0
    for i in range(1, n + 1):
        sum += 1
    return sum

def main():
    n = int(input("Enter a value for n: "))
    print("The sum from 1 to", n, "is", sumToN(n))

main()