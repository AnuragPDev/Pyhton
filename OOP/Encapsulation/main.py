#task is to calcultae the number of students 

# here in this program anyine can change the data which is not acceptable and hence encapsulation comes 

city ="Kotma"
class Student:

    numberOfStudent=0
    school_name="KKSN"
    #instance variabe is a variable which is unique to each object each object have its own cody of variable
    #access modifier we have public and private  
    # __ this maeks data private  
    def __init__(self,name, age ,marks):
        
        self.name=name
        self.age=age
        self.__marks=marks
        
    #using getter 
    def getMarks(self):
        return self.__marks
    #using setter
    def setMarks(self, newMarks,passcode):
        if passcode=="0000":  #security feature 
            self.__marks= newMarks
        else:
            print("Bhaag Yaha se")

    
    
    def show_info(self):
        print(f"{self.name} study in  {self.school_name}, get {self.__marks} in maths, located in {city}")

        
s1=Student("Anurag",27,90)
s2=Student("Animesh", 30,97)
print(s1.getMarks())
s1.setMarks(95,"00")

s1.show_info()

