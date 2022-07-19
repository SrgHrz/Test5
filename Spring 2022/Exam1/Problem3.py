# professor check times
nine_am = 9.0
four_thirty = 4.3
eleven_pm = 11.0

hourEmailSent = int(input("Enter the the hour: "))
minuteEmailSent = int(input("Enter the the minute: "))
amOrPm = input("Enter a for am or p for pm: ")

if amOrPm == 'a':
    if hourEmailSent <= 8.0:
        if minuteEmailSent <= 59:
            print("9:00 AM")
    elif hourEmailSent <= 9:
        if minuteEmailSent <= 0:
            print("9:00 AM")
    else:
        print("4:30 PM")
elif amOrPm == 'p':
    if hourEmailSent <= 4:
        if minuteEmailSent <= 30:
            print("4:30 PM")
    if hourEmailSent < 11:
        if minuteEmailSent < 59:
            print("11:00 PM")
