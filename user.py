
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
    @classmethod
    def check_user(cls, username, phone_number, password):
        """
        checks for registered users
        """
        myuser = ""
        for user in User.user_list:
            if user.username == username and user.password == password and user.phone_number == phone_number:
                myuser == user.username
        return myuser

##################
##################
####################
#@@@@@@@@@@@@@@@@@@@