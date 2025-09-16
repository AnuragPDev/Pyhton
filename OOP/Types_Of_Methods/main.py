# static , class , instance
class Student():
    school ="KKSN"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):   # instance method and we call it using s1.avg()
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getSchoolName(cls):
        cls.school="Hello"
        
        return cls.school
    @staticmethod
    def info():
        print("This is Student Class..")
    


s1=Student(23,23,24)
s2=Student(32,32,12)
print(s1.avg(),s2.avg())
print(Student.info()) # it shows error we need to pass something thats why we will use decprator 
Student.info()
