from cgi import test
import unittest

from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user=User("Mwashe","Berit","mwasheberit@gmail.com","mwasheB","0794163715")

    def test_init(self):
        self.assertEqual(self.new_user.first_Name,"Mwashe")
        self.assertEqual(self.new_user.last_Name,"Berit")
        self.assertEqual(self.new_user.e_mail,"mwasheberit@gmail.com")
        self.assertEqual(self.new_user.user_Name,"mwasheB")
        self.assertEqual(self.new_user.phone_Number,"0794163715")

    def tearDown(self):
        User.user_list=[]
    def test_save_User(self):
        ''''
        we save user
        then assert if it exist in  user list
        '''
        self.new_user.save_User()
        self.assertEqual(len(User.user_list),1)



    # def test_find_User(self):
    #     self.new_user.save_User()
    #     test_user=User("Test","B","testb@gmail.com",'TestB','0711223344')
    #     test_user.save_User()
    #     found_user=User.find_User("testb@gmail.com")
    #     self.assertEqual(found_user.user_Name,test_user.user_Name)
    



    def test_find_User_by_Mail(self):
        self.new_user.save_User()
        test_user=User("Test","user","test@user.com",'TestB',"0711223344") # new contact
        test_user.save_User()
        found_user=User.find_User("test@user.com")
        self.assertEqual(found_user.e_mail,test_user.e_mail)
        self.assertEqual(found_user.phone_Number,test_user.phone_Number)
        self.assertEqual(found_user.first_Name,test_user.first_Name)
        self.assertEqual(found_user.last_Name,test_user.last_Name)

if __name__=='__main__':
    unittest.main()