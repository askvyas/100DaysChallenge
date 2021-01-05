class User:
    def __init__(self,userid,name):
        self.id = userid
        self.uname = name
        #Default
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1=User("0001", "Karthik")
# user_1.usename = "ASKV"
# user_1.id = "001"
print(user_1.following)
print(user_1.followers)
user_2=User("002", "Vyas")
print(user_1.following)
print(user_1.followers)

user_1.follow(user_2)
print(user_2.followers)
print(user_1.following)