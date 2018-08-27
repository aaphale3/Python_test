#This is my first python program. The user inputs a day and month and gets the corresponding zodiac sign.


try:
    day = int(input("Enter numerical day of birth: "))
    month = input("Enter month of birth e.g. january, february, etc.: ")
    if day <= 0 or day > 31:
        print("Invalid day. Please try again.")
    elif month not in("january", "february", "march", "april", "may", "june", "july", "august", "september", \
    "october", "november", "december"):
        print("Invalid month. Please try again.")
    else:
        if (21 <= day <= 31 and month.lower() == "march") or (1 <= day <= 20 and month.lower() == "april"):
            print("Your zodiac sign is Aries.")
        elif (21 <= day <= 30 and month.lower() == "april") or (1 <= day <= 21 and month.lower() == "may"):
            print("Your zodiac sign is Taurus.")
        elif (22 <= day <= 31 and month.lower() == "may") or (1 <= day <= 21 and month.lower() == "june"):
            print("Your zodiac sign is Gemini.")
        elif (22 <= day <= 30 and month.lower() == "june") or (1 <= day <= 22 and month.lower() == "july"):
            print("Your zodiac sign is Cancer.")
        elif (23 <= day <= 31 and month.lower() == "july") or (1 <= day <= 22 and month.lower() == "august"):
            print("Your zodiac sign is Leo.")
        elif (23 <= day <= 31 and month.lower() == "august") or (1 <= day <= 23 and month.lower() == "september"):
            print("Your zodiac sign is Virgo.")
        elif (24 <= day <= 30 and month.lower() == "september") or (1 <= day <= 23 and month.lower() == "october"):
            print("Your zodiac sign is Libra.")
        elif (24 <= day <= 31 and month.lower() == "october") or (1 <= day <= 22 and month.lower() == "november"):
            print("Your zodiac sign is Scorpio.")
        elif (23 <= day <= 30 and month.lower() == "november") or (1 <= day <= 21 and month.lower() == "december"):
            print("Your zodiac sign is Sagittarius.")
        elif (22 <= day <= 31 and month.lower() == "december") or (1 <= day <= 20 and month.lower() == "january"):
            print("Your zodiac sign is Capricorn.")
        elif (21 <= day <= 31 and month.lower() == "january") or (1 <= day <= 19 and month.lower() == "february"):
            print("Your zodiac sign is Aquarius.")
        elif (20 <= day <= 29 and month.lower() == "february") or (1 <= day <= 20 and month.lower() == "march"):
            print("Your zodiac sign is Pisces.")
except ValueError: #ValueError occurs if user enters any character other than positive integer or if nothing is entered
    print("This program only takes numeric values. Exiting... ")
except KeyboardInterrupt: #if operation is canceled (Ctrl - C or clear)
    print("You canceled the operation.")
