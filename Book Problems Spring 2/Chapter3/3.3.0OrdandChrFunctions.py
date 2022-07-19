# ord('character') : gives the (order/number) ASCII code of the character
# chr(number) : gives the character represented by the code

offset = 32
lowercaseLetter = 'h'
uppercaseLetter = chr(ord(lowercaseLetter) - offset)
print(uppercaseLetter)

lowercaseLetter = input("Enter a lowercase letter and the uppercase"
                   "version will be printed: ")
offset = 32
uppercaseLetter = chr(ord(lowercaseLetter) - offset)
print(uppercaseLetter)

