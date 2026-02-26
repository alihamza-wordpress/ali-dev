class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Tesla","S5")
my_new_car = Car("BMW","i7")
print(my_car.brand)
print(my_car.model)

my_new_car1 = Car("BMW", "M5")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car1.brand)
print(my_new_car1.model)