import unittest
from user import User
#from creds import Credentials


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("qwerty", "123456", '!@#$%678' )

    def test_init(self):
        self.assertEqual(self.new_user.username, "qwerty")
        self.assertEqual(self.new_user.phone_number, '123456')
        self.assertEqual(self.new_user.password, "!@#$%678")

    def test_saveu(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == "__main__":
    unittest.main()