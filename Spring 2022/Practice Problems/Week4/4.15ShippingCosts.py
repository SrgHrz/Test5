# Shipping costs are 5 inside the United States,
# except that to Hawaii and Alaska they are 10.
# International shipping costs are 20. Write a program that
# reads in a country and state/province and prints the price
# to ship a package there.

countryName = input("Enter country name: ")
stateOrProvince = input("Enter state/province: ")

if countryName == 'United States':
    if stateOrProvince != 'Alaska' or stateOrProvince != 'Hawaii':
        print("$5")
    else:
        print("$10")
else:
    print("$20")

# HR code:

countryName = input()
stateOrProvince = input()

if countryName == 'United States':
    if stateOrProvince != 'Alaska' or stateOrProvince != 'Hawaii':
        print("$5")
    else:
        print("$10")
else:
    print("$20")