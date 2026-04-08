class Car:
    def __init__(self, brand, model):
        self.__brand = brand #__brand → private variable (cab be only accessed inside class and sub-class but NOT by objects)
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self): #good practice of writing a getter method name with get word. 
        return f"Brand is : {self.__brand}"
    
    def fuel_type(self): #polymorphism (see line: 20)
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size): #no need to write as __brand here in sub-class.
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):  #polymorphism (see line: 12)
        return "Battery"

tesla_car = ElectricCar("Tesla", "Model X", "85 kWh") #ELectricCar object
offroad_car = Car("Land Rover", "Defender") #Car object

print("Tesla: ", tesla_car.fuel_type()) 
print("Defender: ", offroad_car.fuel_type()) 
print(Car.total_car)
