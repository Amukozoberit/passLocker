
from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential=Credentials("bMwashe","12345")
    def test_init(self):
        self.assertEqual(self.new_credential.name,"bMwashe")
        self.assertEqual(self.new_credential.password,"12345")



    def test_save_Credentials(self):
        self.new_credential.save_Credentials()
        self.assertEqual(len(Credentials.cred_list),1)
        
    def test_genPass(self):
        passw=Credentials.genPass(self)
        test_credential=Credentials("Test","{passw}")

        self.assertNotEqual(len(test_credential.password),0)
    
if __name__ == '__main__':
    unittest.main()
    