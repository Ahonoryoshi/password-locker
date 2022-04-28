import unittest
from user import User
from creds import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credential = Credentials('qwer','qwert', "12345", "!@34@#$")

    def test_init(self):
        self.assertEqual(self.new_credential.account, "qwer")
        self.assertEqual(self.new_credential.username, "qwert")
        self.assertEqual(self.new_credential.phone_number, '12345')
        self.assertEqual(self.new_credential.password, "!@34@#$")

    def save_credential_test(self):
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        
        Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
        self.new_credential.save_details()
        test_credential = Credentials("a", "b", "1",'d')
        test_credential.save_details()
        self.assertTrue(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        self.new_credential.save_details()
        test_credential = Credentials("p", "q",'123', "qwertyu")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertTrue(len(Credentials.credentials_list), 1)

    def test_find_credential(self):
        self.new_credential.save_details()
        test_credential = Credentials("x", "y",'124', "qfdvqwhbv")
        test_credential.save_details()

        c = Credentials.find_credential("x")

        self.assertTrue(c.account, test_credential.account)

    def test_credential_exist(self):
        self.new_credential.save_details()
        q = Credentials("asd",'asdfghjkl', "456", "22p49//~~00))")
        q.save_details()
        found = Credentials.if_credential_exist("asd")
        self.assertTrue(found)

    def test_display_creds(self):

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()