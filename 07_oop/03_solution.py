class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car): #ElectricCar class inheriting Car class (All Car class attributes + methods)
    def __init__(self, brand, model, battery_size): 
        super().__init__(brand, model) #initilize variables 
        self.battery_size = battery_size

tesla_car = ElectricCar("Tesla", "Model X", "85 kWh")
print(tesla_car.brand)
print(tesla_car.model)
print(tesla_car.battery_size)
print(tesla_car.full_name()) #DryRun