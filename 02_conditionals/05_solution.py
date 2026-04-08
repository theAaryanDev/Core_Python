#My Approach
weather_input = input("Enter current weather: (sunny/rainy/snowy): ")
weather = weather_input.lower()
if (weather== "sunny"):
    print("Go for a walk")
elif (weather == "rainy"):
    print("Read a book")
elif (weather == "snowy"):
    print("Build a snowman")

#Sir approach
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)