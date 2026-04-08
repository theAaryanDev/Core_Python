#my approach
#partially correct
def cube(num):
    return num**3

print(cube(3))

#Sir approach
#lambda is used to write one-line code that (or say one time use functions)
#--------------------------understand lambda syntax------------------------
# function_name_variable = lambda parameter_name : your_function_working (see ↓)
cube = lambda x: x ** 3

print(cube(3))

#NOTE: #def function VS lambda function
#lambda is used to write one-line code that (or say one time use functions) WHILE, def function is preferred when you have to use that function at multiple locations.
#also. lambda function is preferred in the Frameworks and Libraries of the Python.