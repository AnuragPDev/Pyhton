#class variables are related to class and common for all instance  
class Car:
    
    _no_of_wheels= 4     #class variable 

    def __init__(self):
        self.mil = 10
        self.brand = "BMW"



    def info(self):
        print(f"car: {self.brand}, milege:{self.mil}, and has {Car._no_of_wheels}")

car1 =Car()
car2= Car()

print(Car._no_of_wheels)
# both will print same output 
# print(car1.mil, car1.brand)
# print(car2.mil, car2.brand)

#lets change the milage 
car1.mil=50
car1.info()
car2.info()