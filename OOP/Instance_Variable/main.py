#task is to calcultae the number of students 

city ="Kotma"
class Student:

    numberOfStudent=0
    school_name="KKSN"
    #instance variabe is a variable which is unique to each object each object have its own cody of variable
    def __init__(self,name, age ,marks):
        
        self.name=name
        self.age=age
        self.marks=marks
        
        Student.numberOfStudent = Student.numberOfStudent+1
    
    def show_info(self):
        print(f"{self.name} study in  {self.school_name}, get {self.marks} in maths, located in {city}")

        
s1=Student("Anurag",27,90)
s2=Student("Animesh", 30,97)

s1.show_info()
s2.show_info()