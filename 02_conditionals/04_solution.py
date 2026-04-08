#my approach
# print("Status of Banana:")
# color = "yellow"
# if (color == "green"):
#     print("Banana is Unripe")
# elif (color == "yellow"):
#     print("Banana is Ripe")
# elif (color == "brown"):
#     print("Banana is Overripe")

#My Approach : 2
fruit = input("Please enter the Name of the Fruit: ")
color = int(input("Select Color: \n 1 : Green \n 2 : Yellow \n 3 : Brown\n"))
status = {1 : 'Unripe', 2 : 'Ripe', 3 : 'Overripe'}

print(f"Status of {fruit} is : {status[color]}")

#Sir approach
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
