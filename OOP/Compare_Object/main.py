class Computer:
    def __init__(self):
        self.name="Dell"
        self.age =5 

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1=Computer()
c2=Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")


