# method overloading is the process of creating methods with same name but with different arguments 
# python does not support method overloading
# we can acheive method overloading by making a method which can handle different argumants
class Addition:
# this will handle only two arguments but what if we need to pass sometime 2 and sometimes three argument
    # def sum(self ,a,b):
    #     return a+b
# we can achieve this by using args and kwarg

    def sum(self,*args):
        return sum(args)


# another way to achieve this is by usibg default 
    def addition(self, a=None ,b=None, c=None):
        if a!=None and b!= None and c!=None:
            return (a+b+c)
        elif a!=None and b!=None:
            return a+b
        

add= Addition()
print(add.sum(2,3,4)) 
print(add.sum(2,3)) 
print(add.sum(2,3,4,4)) 
print(add.addition(2,3,4)) 
print(add.addition(2,3)) 
