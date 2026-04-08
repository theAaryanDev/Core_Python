#Lecture 17 : Scopes and Closures in python


# Scope: The region of the program where a vaiable is defined and can be accessed.
# Closure: A function that retains access to variables from its enclosing scope, even after the outer function has finished executing.

username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1) #yes, you can hold a function's return value in a variable, and use it later on the program.
# print(result)

# def func3():
#     global x #this is how you can modify a global variable inside a function, but it's generally not recommended. bad practice
#     x = 12
    
# func3() #you MUST call the function to see the effect of the global variable change, otherwise it won't change.
# print(x)



def f1():
    x = 88
    def f2(): 
        print(x)
    return f2 #notice that we are returning the function itself, not calling it. if we were to call it, it would execute the function and return its result, which is None in this case. By returning the function itself, we can call it later and it will still have access to the variable x, even though f1 has finished executing. This is an example of a closure in python.
myResult = f1()
myResult()


def chaicoder(num):
    def actualFunction(num2):
        return num2 ** num #when you return num here, it also returns the num reference (a bagpack containing all inner variable and outer variables along with their references) | notice that we are using the variable num from the outer function, even though it is not defined in the inner function. This is possible because of closures, which allow the inner function to access variables from its enclosing scope. In this case, the variable num is captured by the closure and can be used inside the actualFunction, even after chaicoder has finished executing.
    return actualFunction #notice that we are returning the inner function itself, not calling it. This allows us to create multiple instances of the inner function with different values of num, which can be used later on in the program. Each instance of the inner function will retain access to its own value of num, thanks to closures. | How we use two returns in a function? We are returning the inner function itself, which is a closure that retains access to the variable num from the outer function. This allows us to create multiple instances of the inner function with different values of num, and each instance will have access to its own value of num, thanks to closures. So, we can use two returns in a function to return both the inner function and its result when called later on in the program.



f = chaicoder(2)
g = chaicoder(3)

print(f(3)) #here, f(3) called f and f called chaicoder(2) (see line: 50)
print(g(3))

#Assignment: closure python gfg