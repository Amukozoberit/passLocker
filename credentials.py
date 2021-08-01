from cgitb import text
from random import choice
import string
from user import User


class Credentials:
    ''''
    class with the pasword locker
    '''
    cred_list=[]
    password:text;
    def __init__(self,name,password):
        '''name and password instance are initialized every time we call credentials'''
        self.name=name
        self.password=password
    
    def save_Credentials(self):
        '''we save the creditaals by pushing code to cred_list'''
        Credentials.cred_list.append(self)

    @classmethod
    def genPass(cls):
        '''generating password'''
        characters=string.ascii_letters+ string.punctuation+ string.digits
        password="".join(choice(characters) for x in range(8,16))
        cls.password=password
        return password
    
    @classmethod
    def display_Credentials(cls):
        '''displays credentials available'''
        return cls.cred_list


    def delete_Account(self):
        '''deletes credentials'''
        Credentials.cred_list.remove(self)
    

    @classmethod
    def check_cred_Exists(cls,name):
        '''checks if credential exists'''
        for userCred in cls.cred_list:
            if userCred.name==name:
                return True
        return False


    @classmethod
    def find_cred(cls,name):
        '''finds credentials'''
        for cred in cls.cred_list:
           if cred.name==name:
               return cred

   
            
        

