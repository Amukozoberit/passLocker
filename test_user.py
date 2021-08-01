from cgi import test
import unittest

from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''setup method called before any test is run
        We create a new user asign value and test if its working fine'''
        self.new_user=User("Mwashe","Berit","mwasheberit@gmail.com","mwasheB","0794163715")

    def test_init(self):
        ''''method runs whenever we instanciate our class
        so every time we instanciate our class we create a user'''
        self.assertEqual(self.new_user.first_Name,"Mwashe")
        self.assertEqual(self.new_user.last_Name,"Berit")
        self.assertEqual(self.new_user.e_mail,"mwasheberit@gmail.com")
        self.assertEqual(self.new_user.user_Name,"mwasheB")
        self.assertEqual(self.new_user.pass_word,"0794163715")

    def tearDown(self):
        '''run after every test to ensure user list never conflicts'''
        User.user_list=[]
    def test_save_User(self):
        ''''
        we save user
        then assert if it exist in  user list
        '''
        self.new_user.save_User()
        self.assertEqual(len(User.user_list),1)


    def test_find_User_by_Pass(self):
        '''find a user by the password they give then assert that each value of the user is the value that is recorded'''
        self.new_user.save_User()
        test_user=User("Test","user","test@user.com",'TestB',"0711223344") # new contact
        test_user.save_User()
        found_user=User.find_User("0711223344")
        self.assertEqual(found_user.e_mail,test_user.e_mail)
        self.assertEqual(found_user.pass_word,test_user.pass_word)
        self.assertEqual(found_user.first_Name,test_user.first_Name)
        self.assertEqual(found_user.last_Name,test_user.last_Name)

        



    
if __name__=='__main__':
    unittest.main()