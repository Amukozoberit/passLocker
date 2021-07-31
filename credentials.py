from random import choice
import string


class Credentials:
    ''''
    class with the pasword locker
    '''
    cred_list=[]
    def __init__(self,name,password):
        self.name=name
        self.password=password
    
    def save_Credentials(self):
        Credentials.cred_list.append(self)


    def genPass(self):
        characters=string.ascii_letters+ string.punctuation+ string.digits
        password="".join(choice(characters) for x in range(8,16))
        # self.password=password
    def display_Credentials(self):
        pass

