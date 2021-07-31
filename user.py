import email


class User:
    user=[]
    '''user Class helps define properties for our class everytime
    we run our class an instant is created with this properties'''
    def __init__(self,first_Name,last_Name,e_mail,user_Name):
        self.first_Name=first_Name
        self.last_Name=last_Name
        self.e_mail=e_mail
        self.user_Name=user_Name
        


    def save_User(self):
        User.user.append(self)

    