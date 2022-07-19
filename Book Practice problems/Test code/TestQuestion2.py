lowerCaseLetter = 'eval(input("Enter a lowercase letter:"))'
offset = 32
uppercaseLetter = chr(ord(lowerCaseLetter) - offset)
print("Upper case letter is", uppercaseLetter)

lowerCaseLetter = input()
offset = 32
uppercaseLetter = chr(ord(lowerCaseLetter) - offset)
print("Upper case letter is", uppercaseLetter)