#This program accepts a string of characters and tells user if he/she has entered a palindrome.

try:
    str = input("Enter a word or name: ")

    if str == "": #checks for no input(null)
        print("Error. Please provide valid input.")
    elif str == str[: : -1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
except KeyboardInterrupt: #if operation is canceled (Ctrl - C or clear)
    print("You canceled the operation.")
