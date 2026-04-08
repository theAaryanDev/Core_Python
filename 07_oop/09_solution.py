class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_petrol_car = Car("Mahindra", "XUV 700") #Car Object 
my_electric_car = ElectricCar("Tesla", "Model X", "85 kWh") #Electric car object

#NOTE: my_petrol_car is an instance of what? → Car
#NOTE: my_electric_car is an instance of what? → Electric Car AND Car (Yes, both)

print(isinstance(my_electric_car, ElectricCar)) #DryRun these ↓ | isinstance(obj, class) verify if obj belongs to class?
print(isinstance(my_electric_car, Car))
print(isinstance(my_petrol_car, ElectricCar))
print(isinstance(my_petrol_car, Car))
