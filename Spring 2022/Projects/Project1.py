# File: Project1.py
# Student: Sergio Hernandez
# UT EID: sh46485
# Course Name: CS303E
#
# Date: 3/8/22
# Description of Program: To create a program which is able to convert between English and metric units

# Defining constants as strings
ONE = "1"
TWO = "2"
THREE = "3"

ERRORMESSAGE = "\nERROR: Answer must be 1, 2 or 3. Try again."

print("")
print("Welcome to the English/Metric conversion utility.")
print("")

print("This utility allows you to convert between English units")
print("(miles, feet, inches) and metric units (kilometers, meters,")
print("centimeters).")
# while loop should go here!!!!
userInput = 2 # used to start the loop
while userInput != THREE:
    print("")
    print("------------------------------------------------------------")
    print("")

    print("Which direction would you like to convert:")
    print("   For English to Metric type: 1")
    print("   For Metric to English type: 2")
    print("   To Quit type:               3")
    print()
    userInput = input("   Input your answer (1, 2, or 3): ")

    # (1) Handles the very first case of 3 (WORKS!!!!!!)
    if userInput == THREE:
        print("")
        print("Thanks for using our converter. Goodbye!")

    # (2) if not the very first case of 3, needs to handle a wrong input -> repeat (WORKS)
    elif (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
        print(ERRORMESSAGE)
        print("")
        ##
        print("Which direction would you like to convert:")
        print("   For English to Metric type: 1")
        print("   For Metric to English type: 2")
        print("   To Quit type:               3")
        print("")
        userInput = input("   Input your answer (1, 2, or 3): ") # (2) Needs to handle 3 -> thanks and, s -> repeat (WORKS!!!!)
        if userInput == THREE: # needs to quit and thanks (Works!!!!!)
            print("")
            print("Thanks for using our converter. Goodbye!")
            # Needs to repeat indefinitely if string (WORKS!!!!!)
        else:
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print("")
                print(ERRORMESSAGE)
                print("")
                ##
                print("Which direction would you like to convert:")
                print("   For English to Metric type: 1")
                print("   For Metric to English type: 2")
                print("   To Quit type:               3")
                print()
                userInput = input("   Input your answer (1, 2, or 3): ")
                ##
                if userInput == ONE: #FAILS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    break
                if userInput == THREE:
                    break
            print()
            print("Thanks for using our converter. Goodbye!")

    # (3) if not a string or three then continue as normal for 1: E->M
    elif userInput == ONE: # E -> M
        print("")
        print("Select English units to convert to metric equivalent:")
        print("   For miles type:  1")
        print("   For feet type:   2")
        print("   For inches type: 3")
        print()
        userInput = input("   Choose English units to convert (1, 2, or 3): ")
        # needs to repeat in case if infinite loop, (WORKS!!!)
        while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
            print(ERRORMESSAGE)
            print("")
            print("Select English units to convert to metric equivalent:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            print()
            # Needs to provide escape (WORKS!!!!!)
            userInput = input("   Choose English units to convert (1, 2, or 3): ")
            if userInput == ONE:
                break
            if userInput == TWO:
                break
            if userInput == THREE:
                break
        if userInput == ONE: # Miles chosen for English
            print("")
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            print("")
            userInput = input("   Choose target metric units (1, 2 or 3): ")
            # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print(ERRORMESSAGE)
                print()
                print("Convert to which metric units:")
                print("   For kilometers type:  1")
                print("   For meters type:      2")
                print("   For centimeters type: 3")
                print()
                userInput = input("   Choose target metric units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # miles to kilometers
                print("")
                miles = float(input("Enter the number of miles to convert to kilometers: "))# needs to handle invalid input
                # if miles != number, == string:
                # print question again
                kilometers = miles * 5280 * 0.3048 * (1 / 1000)
                print("")
                print("RESULT:", miles, "miles = ", format(kilometers, ".3f"), "kilometers")
            elif userInput == TWO: # miles to meters
                print("")
                miles = float(input("Enter the number of miles to convert to meters: "))# needs to handle invalid input
                # if miles != number, == string:
                # print question again
                meters = miles * 5280 * 0.3048
                print("")
                print("RESULT:", miles, "miles = ", format(meters, ".3f"), "meters")
            elif userInput == THREE: # miles to centimeters
                print("")
                miles = float(input("Enter the number of miles to convert to centimeters: "))# needs to handle invalid input
                # if miles != number, == string:
                # print question again
                centimeters = miles * 5280 * 0.3048 * 100
                print("")
                print("RESULT:", miles, "miles = ", format(centimeters, ".3f"), "centimeters")

        elif userInput == TWO: # Feet chosen for English
            print("")
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            print()
            userInput = input("   Choose target metric units (1, 2 or 3): ")
        # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print(ERRORMESSAGE)
                print("")
                print("Convert to which metric units:")
                print("   For kilometers type:  1")
                print("   For meters type:      2")
                print("   For centimeters type: 3")
                print("")
                userInput = input("   Choose target metric units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # Feet to kilometers
                print("")
                feet = float(input("Enter the number of feet to convert to kilometers: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                kilometers = feet * 0.3048 * (1 / 1000)
                print("")
                print("RESULT:", feet, "feet = ", format(kilometers, ".3f"), "kilometers")
            elif userInput == TWO: # feet to meters
                print("")
                feet = float(input("Enter the number of feet to convert to meters: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                meters = feet * 0.3048
                print("")
                print("RESULT:", feet, "feet = ", format(meters, ".3f"), "meters")
            elif userInput == THREE: # feet to centimeters
                print("")
                feet = float(input("Enter the number of feet to convert to centimeters: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                centimeters = feet * 0.3048 * 100
                print("")
                print("RESULT:", feet, "feet = ", format(centimeters, ".3f"), "centimeters")

        elif userInput == THREE: # Inches chosen for English
            print("")
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            print("")
            userInput = input("  Choose target metric units (1, 2 or 3): ")
            # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print(ERRORMESSAGE)
                print("")
                print("Convert to which metric units:")
                print("   For kilometers type:  1")
                print("   For meters type:      2")
                print("   For centimeters type: 3")
                print("")
                userInput = input("   Choose target metric units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # Inches to kilometers
                print("")
                inches = float(input("Enter the number of inches to convert to kilometers: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                kilometers = inches * (1 / 12) * 0.3048 * (1 / 1000)
                print("")
                print("RESULT:", inches, "inches = ", format(kilometers, ".3f"), "kilometers")
            elif userInput == TWO: # inches to meters
                print("")
                inches = float(input("Enter the number of inches to convert to meters: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                meters = inches * (1 / 12) * 0.3048
                print("")
                print("RESULT:", inches, "inches = ", format(meters, ".3f"), "meters")
            elif userInput == THREE: # inches to centimeters
                print("")
                inches = float(input("Enter the number of inches to convert to centimeters: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                centimeters = inches * (1/12) * 0.3048 * 100
                print("")
                print("RESULT:", inches, "inches = ", format(centimeters, ".3f"), "centimeters")

# (4) if not a string or three or 1 then continue as normal for 1: M->E
    elif userInput == TWO: # M -> E
        print("")
        print("Select metric units to convert to English equivalent:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        print()
        userInput = input("   Choose metric units to convert (1, 2, or 3): ")
        # needs to repeat in case if infinite loop, (WORKS!!!)
        while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
            print(ERRORMESSAGE)
            print("")
            print("Select metric units to convert to English equivalent:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3")
            print()
            # Needs to provide escape (WORKS!!!!!)
            userInput = input("   Choose metric units to convert (1, 2, or 3): ")
            if userInput == ONE:
                break
            if userInput == TWO:
                break
            if userInput == THREE:
                break
        if userInput == ONE: # kilometers chosen for metric
            print("")
            print("Convert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            print()
            userInput = input("   Choose target English units (1, 2 or 3): ")
            # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print(ERRORMESSAGE)
                print()
                print("Convert to which English units:")
                print("   For miles type:  1")
                print("   For feet type:   2")
                print("   For inches type: 3")
                print()
                userInput = input("   Choose target English units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # kilometers to miles
                print("")
                kilometers = float(input("Enter the number of kilometers to convert to miles: "))# needs to handle invalid input
                # if miles != number, == string:
                # print question again
                miles = kilometers * 1000 * 3.28084 * (1 / 5280)
                print("")
                print("RESULT:", kilometers, "kilometers = ", format(miles, ".3f"), "miles")
            elif userInput == TWO: # kilometers to feet
                print("")
                kilometers = float(input("Enter the number of kilometers to convert to feet: ")) # needs to handle invalid input
                # if miles != number, == string:
                # print question again
                feet = kilometers * 1000 * 3.28084
                print("")
                print("RESULT:", kilometers, "kilometers = ", format(feet, ".3f"), "feet")
            elif userInput == THREE: # kilometers to inches
                print("")
                kilometers = float(input("Enter the number of kilometers to convert to inches: ")) # needs to handle invalid input
                # if miles != number, == string:
                # print question again
                inches = kilometers * 1000 * 3.28084 * 12
                print("")
                print("RESULT:", kilometers, "kilometers = ", format(inches, ".3f"), "inches")

        elif userInput == TWO: # meters chosen for metric
            print("")
            print("Convert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            print()
            userInput = input("   Choose target English units (1, 2 or 3): ")
        # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print(ERRORMESSAGE)
                print("")
                print("Convert to which English units:")
                print("   For miles type:  1")
                print("   For feet type:   2")
                print("   For inches type: 3")
                print("")
                userInput = input("   Choose target English units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # meters to miles
                print("")
                meters = float(input("Enter the number of meters to convert to miles: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                miles = meters * 3.28084 * (1 / 5280)
                print("")
                print("RESULT:", meters, "meters = ", format(miles, ".3f"), "miles")
            elif userInput == TWO: # meters to feet
                print("")
                meters = float(input("Enter the number of meters to convert to feet: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                feet = meters * 3.28084
                print("")
                print("RESULT:", meters, "meters = ", format(feet, ".3f"), "feet")
            elif userInput == THREE: # meters to inches
                print("")
                meters = float(input("Enter the number of meters to convert to inches: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                inches = meters * 3.28084 * 12
                print("")
                print("RESULT:", meters, "meters = ", format(inches, ".3f"), "inches")

        elif userInput == THREE: # centimeters chosen for metric
            print("")
            print("Convert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            print("")
            userInput = input("   Choose target English units (1, 2 or 3): ")
            # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print(ERRORMESSAGE)
                print("")
                print("Convert to which English units:")
                print("   For miles type:  1")
                print("   For feet type:   2")
                print("   For inches type: 3")
                print("")
                userInput = input("   Choose target English units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # centimeters to miles
                print("")
                centimeters = float(input("Enter the number of centimeters to convert to miles: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                miles = centimeters * (1 / 100) * 3.28084 * ( 1/ 5280)
                print("")
                print("RESULT:", centimeters, "centimeters = ", format(miles, ".3f"), "miles")
            elif userInput == TWO: # centimeters to feet
                print("")
                centimeters = float(input("Enter the number of centimeters to convert to feet: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                feet = centimeters * (1 / 100) * 3.28084
                print("")
                print("RESULT:", centimeters, "centimeters = ", format(feet, ".3f"), "feet")
            elif userInput == THREE: # centimeters to inches
                print("")
                centimeters = float(input("Enter the number of centimeters to convert to inches: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                inches = centimeters * (1 / 100) * 3.28084 * 12
                print("")
                print("RESULT:", centimeters, "centimeters = ", format(inches, ".3f"), "inches")