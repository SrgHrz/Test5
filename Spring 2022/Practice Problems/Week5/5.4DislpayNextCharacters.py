# Write a program that reads in a character and then prints
# out the next 10 characters according to ASCII ordering.
# Input Format:
# The only line of input will contain a single character.

# Enter character
character = input("Enter a character: ")
for i in range(ord(character) + 1, ord(character) + 11):
    letter = chr(i)  # converts the number to a character
    print(letter, end=' ')  # prints character

# HR code
# Enter character
character = input()
for i in range(ord(character) + 1, ord(character) + 11):
    letter = chr(i)  # converts the number to a character
    print(letter, end=' ')  # prints character
