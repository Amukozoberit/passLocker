import unittest

from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user=User("Mwashe","Berit","mwasheberit@gmail.com","mwasheB")

    def test_init(self):
        self.assertEqual(self.new_user.first_Name,"Mwashe")
        self.assertEqual(self.new_user.last_Name,"Berit")
        self.assertEqual(self.new_user.e_mail,"mwasheberit@gmail.com")
        self.assertEqual(self.new_user.user_Name,"mwasheB")
    def test_save_User(self):
        ''''
        we save user
        then assert if it exist in  user list
        '''
        self.new_user.save_User()
        self.assertEqual(len(User.user),1)


        pass
if __name__=='__main__':
    unittest.main()