class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod #static method → can be called via class or object, but has no access to class or instance data | @staticmethod aka decorators
    def general_description(): #NOTE: here no (self) bcz. no need to establish connection b/w class & obj
        return "Cars are the means of transport"

class ElectricCar(Car): #ElectricCar class inheriting Car class (All Car class attributes + methods)
    def __init__(self, brand, model, battery_size): 
        super().__init__(brand, model) #initilize variables 
        self.battery_size = battery_size

tesla_car = ElectricCar("Tesla", "Model X", "85 kWh")
evergreen_car = Car("Suzuki", "Wagonr")

print(tesla_car.general_description()) #OK (Unokay if you comment line:9 @staticmethod)
print(evergreen_car.general_description()) #OK (Unokay if you comment line:9 @staticmethod)
print(Car.general_description()) #OK

