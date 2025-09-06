class User:
    user_count =0  #static attribute

    def __init__(self, username):
        self.username = username
        #everytime when we want to count the number of user we use static attribute 
        User.user_count+=1

    def display_user(self):
        print("username:",self.username)


user = User("Anurag")

user.display_user()
print(User.user_count)

user2 = User("Anurag")

user3 = User("Anurag")
print(User.user_count) 