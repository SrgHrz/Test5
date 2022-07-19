# ord('character') : gives the (order/number) ASCII code of the character
# chr(number) : gives the character represented by the ASCII code/number

# lets see the outputs first:
print("The ASCII value for h is:", ord('h'))
print("The ASCII value for H is:", ord('H'))
print()

# Testing the program
offset = 32
lowercaseLetter = 'h'
uppercaseLetter = chr(ord(lowercaseLetter) - offset)
print(uppercaseLetter)

# This program will translate the a lowercase letter to an uppercase
lowercaseLetter = input("Enter a lowercase letter and the uppercase"
                   "version will be printed: ")
offset = 32
uppercaseLetter = chr(ord(lowercaseLetter) - offset)
print(uppercaseLetter)

