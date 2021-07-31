from random import choice
import string
from run import main
from credentials import Credentials
import unittest
import credentials 

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential=Credentials("bMwashe","12345")
    def test_init(self):
        self.assertEqual(self.new_credential.name,"bMwashe")
        self.assertEqual(self.new_credential.password,"12345")

    def test_genPass(self):
        self.new_credential=Credentials("Test",Credentials.genPass())
        self.assertTrue(Credentials.genPass())
    
if __name__ == '__main__':
    unittest.main()
    