# instance variables are related to object and its different for different object or instance
class Car:

    def __init__(self):
        self.mil = 10
        self.brand = "BMW"

car1 =Car()
car2= Car()
# both will print same output 
print(car1.mil, car1.brand)
print(car2.mil, car2.brand)

#lets change the milage 
car1.mil=50

print(car1.mil, car1.brand)
print(car2.mil, car2.brand)