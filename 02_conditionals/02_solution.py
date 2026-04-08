#my approach
day = int(input("Select Day: \n 1 → Sun \n 2 → Mon \n 3 → Tue \n 4 → Wed \n 5 → Thur \n 6 → Fri \n 7 → Sat \n"))
age = int(input("Enter Age: "))
price_for_kids = 8
price_for_adults = 12

if day == 4:
    if age < 0:
        print("Invalid Age")
    elif age < 18:
        print(f"Price is: ${price_for_kids - 2}")
    else:
        print(f"Price is: ${price_for_adults - 2}")
else:
    if age < 0:
        print("Invalid Age")
    elif age < 18:
        print(f"Price is: ${price_for_kids}")
    else:
        print(f"Price is: ${price_for_adults}")

#Sir Approach
age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)
