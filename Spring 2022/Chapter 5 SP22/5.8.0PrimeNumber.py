NUMBER_OF_PRIMES = 50 # Total number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 primes per line
count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness other than 1
           # since we know that very number is divisible by one
print("The first 50 prime numbers are")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    isPrime = True  # Is the current number prime?

    # Test if the number is prime
    divisor = 2 # the initial number you divide with-> n/2, n/3, n/4....
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, the number is not prime
            isPrime = False # Set isPrime to false
            break # exit the loop
        divisor += 1

    # Display the prime number and increase count
    if isPrime:
        count += 1  # Increase the count by one

        print(format(number, "5d"), end = '')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print()  # Jump to the new line

    # Check if the next number is prime
    number += 1