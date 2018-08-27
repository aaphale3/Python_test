#This program accepts a string of alphabetical characters and tells user if a palindrome has been entered.

try:
    str = input("Enter a word or name: ")

    if str == "" or not str.isalpha(): #checks for no input(null) and non-alphabetical characters
        print("Error. Please provide valid input.")
    elif str == str[: : -1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
except KeyboardInterrupt: #if operation is canceled (Ctrl - C or clear)
    print("You canceled the operation.")
