# #my approach
# class Battery():
#     battery = "85 kWh"
# class Engine():
#     engine = "super engine"
# class ElectricCar(Battery, Engine):
#     def __init__(self):
#         super().__init__()


# my_car = ElectricCar()

# print(my_car.battery, my_car.engine)

#my approach 2 : failed!
# class Battery:
#     def __init__(self, battery_size):
#         self.battery = battery_size #here, variable name = battery NOT battery_size (think like battery → main variable, battery_size → like placeholder)
    
# class Engine:
#     def __init__(self, engine):
#         self.engine = engine
    
# class ElectricCar(Battery, Engine):
#     def __init__(self, battery, engine):
#         # super().__init__(battery, engine) #error (bcz there is two parent, you can NOT use super() fix↓)
#         Battery.__init__(self, battery) #NOTE: in single-inheritance, we use parenthesis → super().__init__(), but here in multiple-inheritance we do NOT use parenthesis → Battery.__init__()
#         Engine.__init__(self, engine)

# my_car_object = ElectricCar("85 kWh", "DC engine")

# print(isinstance(my_car_object, ElectricCar))
# print(isinstance(my_car_object, Battery))
# print(isinstance(my_car_object, Engine))
# print(my_car_object.battery, my_car_object.engine)

#Sir approach
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

#-------------------------Lecture 18: Object Oriented Programming in Python end-------------------------