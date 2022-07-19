# Cookies problem
eggs = int(input("Enter amount of eggs: "))
cupsOfSugar = float(input("Enter the cups of sugar: "))
cupsOfFlour = float(input("Enter the cups of flour: "))

# For 1 batch of cookies
REQUIRED_EGGS = 4
REQUIRED_SUGAR = 3.3
REQUIRED_FLOUR = 5.9

cookiesFromEggs = eggs / REQUIRED_EGGS
cookiesFromSugar = cupsOfSugar / REQUIRED_SUGAR
cookiesFromFlour = cupsOfFlour / REQUIRED_FLOUR

print("Cookies from egg:", cookiesFromEggs)
print("Cookies from sugar:", cookiesFromSugar)
print("Cookies from flour:", cookiesFromFlour)

if cookiesFromEggs < cookiesFromSugar and cookiesFromEggs < cookiesFromFlour:
    print(round(cookiesFromEggs))
elif cookiesFromSugar <= cookiesFromEggs and cookiesFromSugar < cookiesFromFlour:
    print(round(cookiesFromSugar))
elif cookiesFromFlour < cookiesFromEggs and cookiesFromFlour < cookiesFromSugar:
    print(round(cookiesFromFlour))
