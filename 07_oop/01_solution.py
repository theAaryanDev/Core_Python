#Lecture 18: Object Oriented Programming in Python
# Github Repo : https://github.com/hiteshchoudhary/chai-aur-python/


#NOTE: 1. syntax: just like def → define function, class → class creation
#NOTE: 2. always practice to write class variable in Capital letter. (i.e class Car NOT class car)
#NOTE: Constructor → line: 12
#NOTE: __init__ → line: 12
#NOTE: .self → line: 12
#NOTE: Attribute → line: 13
#NOTE: Instance → line: 17

class Car:
    def __init__(self, user_brand, user_model): #__init__ is fixed varibale, used in case when you want to pass some values aka parameters during objects creation time to reflect that in class for eg → Car ("Toyota", "Corolla") to pass these two you must follow this syntax def __init__(): (init aka constructor in python) | self → set up linkage/context (telephone communication) between class and its objects. without self, we won't be able to access the variables and methods of the class. (like THIS → in JavaScript, SELF → in Python) | user_brand and user_model are parameters.   
        self.brand = user_brand #self.brand is an instance variable (Difference b/w brand VS self.brand? brand → means you are talking about any random varibale, BUT self.brand → means that you are only taking about the the variable that belongs exclusively of that class. this variable is aka Attributes) | user_brand is taking reference from the parameter. it is a parameter which is passed when we create an instance of the class. 
        self.model = user_model

#Calling class is just like calling a function ↓ | we also need to store it into some variable
my_fav_car = Car("Bugatti", "La Voiture Noire") #instance of a class
print(my_fav_car) #<__main__.Car object at 0x000002D79B2C7230> | You must define what to print ↓
print(my_fav_car.brand, my_fav_car.model)

my_fav_suv = Car("Land Rover", "Defender") #you can create infinite objects (instances) of same class
print(my_fav_suv.model)

