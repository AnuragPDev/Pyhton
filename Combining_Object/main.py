class Dog:
    def __init__(self,name ,breed , owner):
        self.name=name 
        self.breed=breed
        self.owner=owner
        print(owner)    
    def bark(self):
        print("Woof-Woof")
    
    def print_dog(dog_obj): # passing object as an argument
        print(dog_obj.name , dog_obj.breed)

class Owner:
    def __init__(self, name , address , contact):
        self.name=name 
        self.address=address
        self.contact=contact

own1 =Owner("Anurag","Tokyo", 8924802)
dog1=Dog("Jecky", "Pitbull",own1)
print(dog1.name, dog1.breed)
dog1.bark()
dog1.print_dog()
print(dog1.owner.name)