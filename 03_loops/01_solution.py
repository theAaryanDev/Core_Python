#Lec 14: Solve 10 loops problem in python
# Github Repo : https://github.com/hiteshchoudhary/chai-aur-python/


#My Approach
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_numbers = 0
for i in numbers:
    if i > 0:
        positive_numbers += 1

print(positive_numbers)

#Sir Approach
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1

print("Final count of Positive number is: ", positive_number_count)