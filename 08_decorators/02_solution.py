def debug(func):
    def wrapper(*args, **kwargs):
        # args_value = ', '.join(str(arg) for arg in args)
        # kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling function: {func.__name__} with Arguments are: {args}, and the Keywords Arguments are: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello(*args, **kwargs):
    return args, kwargs

hello("Aryan", "Era", name = "Arya", username= "3R4Z3R")



#-----------------------------------------------note start-------------------------------------------
#NOTE: Non-default arguments → first, Default arguments → after (i.e ↓)
# def greet(name, greeting="Hello"): #correct order
# def greet(greeting="Hello", name): #wrong order
# def greet(*, greeting="Hello", name): #using wrong order forcefully (but to call it, you must specify argument with parameter name i.e. greet(name = "Aryan"))
#     print(f"{greeting} {name}, Nice to meet you!")

# greet("Aryan")
# greet(name = "Aryan")
#--------------------------------------------note end-----------------------------------------------