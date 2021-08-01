


class User:
    user_list=[]
    '''user Class helps define properties for our class everytime
    we run our class an instant is created with this properties'''
    def __init__(self,first_Name,last_Name,e_mail,user_Name,pass_word):
        self.first_Name=first_Name
        self.last_Name=last_Name
        self.e_mail=e_mail
        self.user_Name=user_Name
        self.pass_word=pass_word
   
  
    def save_User(self):
        '''function to save a user'''
        User.user_list.append(self)


    @classmethod
    def display_Users(cls):
        return cls.user_list


    @classmethod
    def find_User(cls,pass_word):
        '''cls means its a class method it can be accesd in a class
        check if contact exists with email'''
        for user in cls.user_list:
            if user.pass_word==pass_word:
                return user

  

