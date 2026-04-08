#my approach
#failed
# def greet(name, "sam"):
#     return("Welcome", name)

# print(greet())

#Sir approach
def greet(name = "Sam"):  #remember this
    return "Hello, " + name + " !"


print(greet("chai"))
print(greet())