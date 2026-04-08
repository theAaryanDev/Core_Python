class Car:
    def __init__(self, brand, model):
        self.__brand = brand #__brand → private variable (cab be only accessed inside class and sub-class but NOT by objects)
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self): #good practice of writing a getter method name with get word. 
        return f"Brand is : {self.__brand}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size): #no need to write as __brand here in sub-class.
        super().__init__(brand, model)
        self.battery_size = battery_size

tesla_car = ElectricCar("Tesla", "Model X", "85 kWh")
# print(tesla_car.brand) #attribute error
print(tesla_car.get_brand()) 

#Assignment: Setter in python gfg/stackoverflow