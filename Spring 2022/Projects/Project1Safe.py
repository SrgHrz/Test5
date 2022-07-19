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

    print("Which direction would you like to convert:\n",
          "\t For English to Metric type: 1\n",
          "\t For Metric to English type: 2\n",
          "\t To Quit type:               3")
    print()
    userInput = input("     Input your answer (1, 2, or 3): ")

    # (1) Handles the very first case of 3 (WORKS!!!!!!)
    if userInput == THREE:
        print("")
        print("Thanks for using our converter. Goodbye!")

    # (2) if not the very first case of 3, needs to handle a wrong input -> repeat (WORKS)
    elif (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
        print(ERRORMESSAGE)
        print("")
        print("Which direction would you like to convert:\n",
              "\t For English to Metric type: 1\n",
              "\t For Metric to English type: 2\n",
              "\t To Quit type:               3")
        print()
        userInput = input("     Input your answer (1, 2, or 3): ") # (2) Needs to handle 3 -> thanks and, s -> repeat (WORKS!!!!)
        if userInput == THREE: # needs to quit and thanks (Works!!!!!)
            print("")
            print("Thanks for using our converter. Goodbye!")
            # Needs to repeat indefinitely if string (WORKS!!!!!)
        else:
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print("")
                print(ERRORMESSAGE)
                print("")
                print("Which direction would you like to convert:\n",
                      "\t For English to Metric type: 1\n",
                      "\t For Metric to English type: 2\n",
                      "\t To Quit type:               3")
                print()
                userInput = input("     Input your answer (1, 2, or 3): ")

                if userInput == ONE: #FAILS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    break
                if userInput == THREE:
                    break
            print()
            print("Thanks for using our converter. Goodbye!")

    # (3) if not a string or three then continue as normal for 1: E->M
    elif userInput == ONE: # E -> M
        print("")
        print("Select English units to convert to metric equivalent:\n",
              "\t For miles type: 1\n",
              "\t For feet type:  2\n",
              "\t For inches type: 3")
        print()
        userInput = input("     Choose English units to convert (1, 2, or 3): ")
        # needs to repeat in case if infinite loop, (WORKS!!!)
        while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
            print("")
            print(ERRORMESSAGE)
            print("")
            print("Select English units to convert to metric equivalent:\n",
                  "\t For miles type: 1\n",
                  "\t For feet type:  2\n",
                  "\t For inches type: 3")
            print()
            # Needs to provide escape (WORKS!!!!!)
            userInput = input(     "Choose English unit to convert (1, 2, or 3): ")
            if userInput == ONE:
                break
            if userInput == TWO:
                break
            if userInput == THREE:
                break
        if userInput == ONE: # Miles chosen for English
            print("")
            print("Convert to which metric units:\n",
                  "\t For kilometers type:  1\n",
                  "\t For meters type:      2\n",
                  "\t For centimeters type: 3")
            print()
            userInput = input("     Choose target metric units (1, 2 or 3): ")
            # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print()
                print(ERRORMESSAGE)
                print()
                print("Convert to which metric units:\n",
                      "\t For kilometers type:  1\n",
                      "\t For meters type:      2\n",
                      "\t For centimeters type: 3")
                print()
                userInput = input("     Choose target metric units (1, 2 or 3): ")
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
                miles = float(input("     Enter the number of miles to convert to meters: "))# needs to handle invalid input
                # if miles != number, == string:
                # print question again
                meters = miles * 5280 * 0.3048
                print("")
                print("RESULT:", miles, "miles = ", format(meters, ".3f"), "meters")
            elif userInput == THREE: # miles to centimeters
                print("")
                miles = float(input("     Enter the number of miles to convert to centimeters: "))# needs to handle invalid input
                # if miles != number, == string:
                # print question again
                centimeters = miles * 5280 * 0.3048 * (1 / 100)
                print("")
                print("RESULT:", miles, "miles = ", format(centimeters, ".3f"), "centimeters")

        elif userInput == TWO: # Feet chosen for English
            print("")
            print("Convert to which metric units:\n",
                  "\t For kilometers type:  1\n",
                  "\t For meters type:      2\n",
                  "\t For centimeters type: 3")
            print()
            userInput = input("Choose target metric units (1, 2 or 3): ")
        # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print("")
                print(ERRORMESSAGE)
                print("")
                print("Convert to which metric units:\n",
                      "\t For kilometers type:  1\n",
                      "\t For meters type:      2\n",
                      "\t For centimeters type: 3")
                print("")
                userInput = input("Choose target metric units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # Feet to kilometers
                print("")
                feet = float(input("     Enter the number of feet to convert to kilometers: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                kilometers = feet * 0.3048  * (1 / 1000)
                print("")
                print("RESULT:", feet, "feet = ", format(kilometers, ".3f"), "kilometers")
            elif userInput == TWO: # feet to meters
                print("")
                feet = float(input("     Enter the number of feet to convert to meters: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                meters = feet * 0.3048
                print("")
                print("RESULT:", feet, "feet = ", format(meters, ".3f"), "meters")
            elif userInput == THREE: # feet to centimeters
                print("")
                feet = float(input("     Enter the number of feet to convert to centimeters: "))# needs to handle invalid input
                # if feet != number, == string:
                # print question again
                centimeters = feet * 0.3048 * 100
                print("")
                print("RESULT:", feet, "feet = ", format(centimeters, ".3f"), "centimeters")

        elif userInput == THREE: # Inches chosen for English
            print("")
            print("Convert to which metric units:\n",
                  "\t For kilometers type:  1\n",
                  "\t For meters type:      2\n",
                  "\t For centimeters type: 3")
            print("")
            userInput = input("     Choose target metric units (1, 2 or 3): ")
            # needs to loop for wrong input (WORKS!!!)
            while (userInput != ONE) and (userInput != TWO) and (userInput != THREE):
                print("")
                print(ERRORMESSAGE)
                print("")
                print("Convert to which metric units:\n",
                      "\t For kilometers type:  1\n",
                      "\t For meters type:      2\n",
                      "\t For centimeters type: 3")
                print("")
                userInput = input("     Choose target metric units (1, 2 or 3): ")
                if userInput == ONE:
                    break
                if userInput == TWO:
                    break
                if userInput == THREE:
                    break
            if userInput == ONE: # Inches to kilometers
                print("")
                inches = float(input("     Enter the number of inches to convert to kilometers: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                kilometers = inches * (1 / 12) * 0.3048 * (1 / 1000)
                print("")
                print("RESULT:", inches, "inches = ", format(kilometers, ".3f"), "kilometers")
            elif userInput == TWO: # inches to meters
                print("")
                inches = float(input("     Enter the number of inches to convert to meters: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                meters = inches * (1 / 12) * 0.3048
                print("")
                print("RESULT:", inches, "inches = ", format(meters, ".3f"), "meters")
            elif userInput == THREE: # inches to centimeters
                print("")
                inches = float(input("     Enter the number of inches to convert to centimeters: "))# needs to handle invalid input
                # if inches != number, == string:
                # print question again
                centimeters = inches * (1/12) * 0.3048 * 100
                print("")
                print("RESULT:", inches, "inches = ", format(centimeters, ".3f"), "centimeters")

# (4) if not a string or three or 1 then continue as normal for 1: M->E
