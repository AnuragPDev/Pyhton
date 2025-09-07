from datetime import datetime
class User:
    def __init__(self, username,email, password):
        self.username=username
        self._email= email      # we cant read this attribute should not be used outside the class or in subclass Protected
        self.password=password
        
  # python       
# does not enforce strict rule unlike other language 
    # def clean_email(self):
    #     return self._email.strip().lower()   # strip remove leading and trail spaces
    
    def get_email(self):
        print(f'Email accessed at{datetime.now()}')
        return self._email
    
    def set_email(self, newEmail):
        #validation
        if "@" in newEmail:
            self._email =newEmail
            print(f'Email changed at{datetime.now()}')
        else:
            print("invalid email")

# if we make out instance private internally python do data mangling ie its changed the name of the attribute    

    
user1= User("Anurag","anurag@gmail.com", "123")

print(user1.get_email())
# user1.email="a"   # we dont waht someone to change it and its a bad case 
# print(user1.email)
user1.set_email("apoutlook.com")
print(user1.get_email())


