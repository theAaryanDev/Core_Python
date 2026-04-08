#Lecture 19: What are decorators in python

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time #function ran for this much time
        # print(f'Function {func} ran for {duration} seconds') #DryRun
        print(f'Function {func.__name__} ran for {duration} seconds') #DryRun | .__name__ is an in-build python function to access name.
        return result
    return wrapper

@timer #decorators (my_func will always travel through timer)
def my_func(n):
    time.sleep(n) #sleep for n sec 

timer(my_func(2))

#NOTE: this (function-inside-function "line: 3-4") is Basic Syntax for making a time-calculator-function (timer)



#---------------------------------Bareminimum Decorators Boilerplate start--------------------------
# def decorator(func): #s1
#     def wrapper(*args, **kwargs): #s2
        
#         # wite_your_programme_here

#         result = func(*args, **kwargs) #s3
#         return result #s4
#     return wrapper #s5

# @decorator #s2.2
# def your_general_function(your_parameter, your_keword_parameter) #s2.1 (making a general function)

# your_general_function(your_arguments) #s3.1 (calling the function)
#-----------------------------------------Boilerplate end-------------------------------------------