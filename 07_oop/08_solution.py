class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model #step 1: making model private
    
    @property #step 2: using @property decorator for doing so
    def view_model(self): 
        return self.__model 

my_car = Car("Mahindra", "XUV 700")

# print(my_car.__model) #error bcz. now its private
print(my_car.view_model) #step 3: calling that method (NOTE: even through view_model() seems an function don't use executer here i.e. CORRECT → my_car.view_model, WRONG → my_car.view_model())
