#This program accepts a range of positive integers less than or equal to 500 from the user and prints a list of prime numbers.

try:
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    if start <= 0 or end <=0: #checks for negative values
        print("Please enter an integer greater than 0.")
    elif start > end:
        print("Your start number should be less than your end number.")
    elif end > 500:
        print("Please choose a number less than 500.")
    else:
        all_nums = list(range(start, end))
        prime_list = list(range(start, end))
        for num in all_nums:
            if num in (2, 3, 5, 7, 11, 13, 17, 19):
                continue
            elif (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0) or \
                 (num % 11 == 0) or (num % 13 == 0) or (num % 17 == 0) or (num % 19 == 0):
                prime_list.remove(num)

        print(prime_list)
except ValueError: #ValueError occurs if user enters any character other than positive integer or if nothing is entered
    print("Please enter an integer greater than 0.")
except KeyboardInterrupt: #if operation is canceled (Ctrl - C or clear)
    print("You canceled the operation.")
