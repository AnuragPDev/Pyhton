from datetime import datetime
class User:
    def __init__(self, username,email, password):
        self.username=username
        self._email= email      
        self.password=password

# another wat to use getter and setter method is by decorators 

# for getting the value we use property decorator 
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, newEmail):
        if "@" in newEmail:
            self._email=newEmail
        else:
            print("invalid")
    
    
    
    
user1= User("Anurag","anurag@gmail.com", "123")
print(user1.email) # here we can access the getter method as a property or attribute 
# any change in code in future wont affect this since we are call

user1.email="anuragg@outlook"
print(user1.email)


