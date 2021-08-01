
from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        '''setup function that runs everytime a test is run
    '''
        self.new_credential=Credentials("bMwashe","12345")
    def test_init(self):
        '''test run to check if the app is initialized properly'''
        self.assertEqual(self.new_credential.name,"bMwashe")
        self.assertEqual(self.new_credential.password,"12345")



    def test_save_Credentials(self):
        '''test to check if credentials can be saved'''
        self.new_credential.save_Credentials()
        self.assertEqual(len(Credentials.cred_list),1)
        
    def test_genPass(self):
        '''test to check if generate pasword function is generating a password'''

        passw=Credentials.genPass()
        test_credential=Credentials("Test","{passw}")

        self.assertNotEqual(len(test_credential.password),0)
    

    def tearDown(self):
        ''''''
        Credentials.cred_list=[]
     
    def test_display_Cred(self):
        passw=Credentials.genPass()
        test_credential=Credentials("Test","{passw}")

        self.assertEqual(Credentials.display_Credentials(),Credentials.cred_list)


    def test_delete_Cred(self):
        self.new_credential.save_Credentials()
        passw=Credentials.genPass()
        test_credential=Credentials("Test","{passw}")
        test_credential.save_Credentials()

        test_credential.delete_Account()
        self.assertEqual(len(Credentials.cred_list),1)


    def test_cred_Exists(self):
        self.new_credential.save_Credentials()
        passw=Credentials.genPass()
        test_credential=Credentials("Test","{passw}")
        test_credential.save_Credentials()
        cred_exixts=Credentials.check_cred_Exists("Test")
        self.assertTrue(cred_exixts)

    def test_find_cred(self):

        self.new_credential.save_Credentials()
        passw=Credentials.genPass()
        test_credential=Credentials("Test","{passw}")
        test_credential.save_Credentials()
        cred_found=Credentials.find_cred("Test")
        self.assertEqual(cred_found.name,test_credential.name)

if __name__ == '__main__':
    unittest.main()
    