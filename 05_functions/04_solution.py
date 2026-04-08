#My approach
pi = (22/7)
def circle_measurement (radius):
    circumference = 2 * pi * radius
    area = pi * (radius**2)
    print(f"Circumference of the circle of radius {radius} is : {circumference} and area is : {area}")

circle_measurement(7)

#Sir approach
import math

def circle_stats(radius):
    area = math.pi * radius ** 2 #see how to use any object of a library (math.pi)
    circumference = 2 * math.pi * radius
    return area, circumference #you can return multiple values.

a, c = circle_stats(3) #handling returns (two variables "a and c" because 2 returns is coming from function)

print("Area: ", a, "Circumference: ", c)

#Asssignment: make long dedcimal to two or three decimal places (2.123456 → 2.12) HOW?
