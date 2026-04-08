#My approach
distance = int(input("Enter your distance in KM: "))
if distance < 3:
    mode = "Walk"
elif distance < 15:
    mode = "Bike"
elif distance >= 15:
    mode = "Car"
print("You can use", mode)

#Sir approach
distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of: ", transport)