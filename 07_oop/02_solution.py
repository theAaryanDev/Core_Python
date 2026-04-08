class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self): #self to access brand/model | full_name() is a function but in big picture of class full_name() is a method of this class.
        return f"{self.brand} {self.model}" #NOTE: {self.brand} is Correct , only {brand} is Wrong

evergreen_car = Car("Suzuki", "Wagonr")
print(evergreen_car.brand, evergreen_car.model)
print(evergreen_car.full_name()) #.full_name() NOT .full_name as it a method.