
import random
import string



class User:
    """
    generates User instance
    """

    

    def __init__(self, username,phone_number, password):
        """
        method that defines the properties of user
        """
        self.username = username
        self.phone_number = phone_number
        self.password = password

    user_list = []

    def save_user(self):
        """
        saves a new user account
        """
        User.user_list.append(self)

    
    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        deletes a  saved account by removing it from user_list
        """
        User.user_list.remove(
            self
        )

##################
##################
####################
#@@@@@@@@@@@@@@@@@@@