class Car:
    # brand = None 
    # model = None
    def __init__(self,userbrand,usermodel):
        self.brand = userbrand
        self.model = usermodel
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand = brand
        # self.model = model
        super().__init__(brand,model)
        self.battery = battery_size


my_tesla = ElectricCar("Tesla","Model S", "85kWh")
print(my_tesla.full_name())


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)