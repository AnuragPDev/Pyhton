class User:             # parent , base 
    # def __init__(self,name, id):
    #     self.name = name 
    #     self.id =id 

    def  login(self):
       print("Logged in")

    def _logout(self):
        print("Logged out")
    
    def _property(self):
        print("Its your property")


class Teacher:
    pass


class Student(User):  # here we extend the class of parents 
    def play(self):
        print("Student is playing")


s1=Student()
s1.login()
s1._logout() # here we can use logout functuon from parents class because its public 
s1.play()
s1._property()

u1=User()
# u1.play() parent class cant access child attributes and methods 

