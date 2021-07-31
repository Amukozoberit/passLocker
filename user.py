import email


class User:
    user_list=[]
    '''user Class helps define properties for our class everytime
    we run our class an instant is created with this properties'''
    def __init__(self,first_Name,last_Name,e_mail,user_Name,phone_Number):
        self.first_Name=first_Name
        self.last_Name=last_Name
        self.e_mail=e_mail
        self.user_Name=user_Name
        self.phone_Number=phone_Number
   
  
    def save_User(self):
        User.user_list.append(self)



    @classmethod
    def find_User(cls,email):
        '''check if contact exists with email'''
        for user in cls.user_list:
            if user.e_mail==email:
                return user
        

