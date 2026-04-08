class Car:
    total_car = 0 #object counter initially 0
    
    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model
        Car.total_car += 1 #adding value 1 every time the initilizer (__init__) will be called | why we write Car.total_car instead of self.total_car because we want to access the class variable not instance variable. | why we this statement in initilizer not outside the def or in other method because we want to count the total number of objects created and every time an object is created the it is guaranteed that theinitilizer will be called and the counter will be increased by 1.

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return f"Brand is : {self.__brand}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

tesla_car = ElectricCar("Tesla", "Model X", "85 kWh") #obj1 (Yes, subclass object also counts)
offroad_car = Car("Land Rover", "Defender") #obj2
test_car_1 = Car("test", "test") #obj3
test_car_2 = Car("test", "test") #obj4
test_car_3 = Car("test", "test") #obj5
Car("test", "test") #obj6 (yes this counts too. (NOT necessory whether you hold it or not in variable.)

print(Car.total_car) #DryRun