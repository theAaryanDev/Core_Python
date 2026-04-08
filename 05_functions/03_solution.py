#My approach
def multiply(a, b):
    return a*b

print(multiply(3, 2))
print(multiply("Aryan", 5))
# print(multiply("Aryan", "5")) #error
print(multiply(5, "Aryan")) #DRY

#Sir approach
def add(numOne, numTwo):
    return numOne + numTwo


print(add(5, 5))
