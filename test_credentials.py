
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
    

    def tearDown(self):
        Credentials.cred_list=[]
     
    def test_display_Cred(self):
        passw=Credentials.genPass(self)
        test_credential=Credentials("Test","{passw}")

        self.assertEqual(Credentials.display_Credentials(),Credentials.cred_list)


    def test_delete_Cred(self):
        self.new_credential.save_Credentials()
        passw=Credentials.genPass(self)
        test_credential=Credentials("Test","{passw}")
        test_credential.save_Credentials()

        self.new_credential.delete_Account()
        self.assertEqual(len(Credentials.cred_list),1)


    def test_cred_Exists(self):
        self.new_credential.save_Credentials()
        passw=Credentials.genPass(self)
        test_credential=Credentials("Test","{passw}")
        test_credential.save_Credentials()
        cred_exixts=Credentials.check_cred_Exists("Test")
        self.assertTrue(cred_exixts)

if __name__ == '__main__':
    unittest.main()
    