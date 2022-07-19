# Write a program that reads in a number n and prints out the
# given number n, except if the number n is a multiple of three
# it should output "Fizz" instead of the number, and if n is a
# multiple of five it should output "Buzz" instead of the number.
# If n is a multiple of both three and five, it should
# output "FizzBuzz".

number = int(input("Enter an integer: "))

if number % 3 == 0 and number % 5 != 0:
    print("Fizz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
else:
    print(number)

# HR code
number = int(input())

if number % 3 == 0 and number % 5 != 0:
    print("Fizz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
else:
    print(number)