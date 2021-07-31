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

if __name__=='__main__':
    unittest.main()