all_nums = list(range(2, 101)) 
prime_list = list(range(2, 101))
for num in all_nums:
    if num in (2, 3, 5, 7):
        continue
    elif (num % 5 == 0) or (num % 3 == 0) or (num % 2 == 0) or (num % 7 == 0):
        prime_list.remove(num)

print(len(prime_list))
