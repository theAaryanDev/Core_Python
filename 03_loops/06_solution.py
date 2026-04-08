#My Approach
#---------------------------------------------failed---------------------------------
# number = 0
# while (number < 5):
#     for i in range (number):
#         print(number * i)
#     number += 1

#Sir Approach
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)