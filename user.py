import email


class User:
    '''user Class helps define properties for our objects'''
    def __init__(self,first_Name,last_Name,e_mail,user_Name):
        self.first_Name=first_Name
        self.last_Name=last_Name
        self.e_mail=e_mail
        self.user_Name=user_Name
        