from random import choice
import string


class Credentials:
    ''''
    class with the pasword locker
    '''
    def __init__(self,name,password):
        self.name=name
        self.password=password
    


    def genPass(self):
        characters=string.ascii_letters+ string.punctuation+ string.digits
        password="".join(choice(characters) for x in range(8,16))
        return password
        
