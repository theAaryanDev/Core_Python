import time

def cache(func):
    cached_value = {}
    print(f"Cached values are:\n{cached_value}")
    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        result = func(*args)
        cached_value[args] = result
        return result
    return wrapper

@cache
def long_function(num1, num2):
    time.sleep(2)
    return num1 + num2

print(long_function(2, 3))
print(long_function(3, 4))

#---------------------Lecture 19: What are decorators in python end---------------------------------------