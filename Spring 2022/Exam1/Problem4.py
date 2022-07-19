import math
numberOfItems = int(input("Enter the number of items: "))

if numberOfItems == 5:
    n1 = float(input("Enter price 1: "))
    n2 = float(input("Enter price 2: "))
    n3 = float(input("Enter price 3: "))
    n4 = float(input("Enter price 4: "))
    n5 = float(input("Enter price 5: "))
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        print(1)
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        print(2)
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        print(3)
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        print(4)
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        print(5)
elif numberOfItems == 1:
    n1 = float(input("Enter price 1: "))
    print(1)
elif numberOfItems == 3:
    n1 = float(input("Enter price 1: "))
    n2 = float(input("Enter price 2: "))
    n3 = float(input("Enter price 3: "))
    if n1 > n2 and n1 > n3:
        print(1)
    elif n2 > n1 and n2 > n3:
        print(2)
    elif n3 > n1 and n3 > n2:
        print(3)