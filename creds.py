from user import User
import string
import random
import numbers


class Credentials:
    """
    Class to create account instances
    """

    credentials_list = [] #an empty credentials list 
    def __init__(self, account, username,phone_number, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.username = username
        self.phone_number = phone_number
        self.password = password



    

    def save_details(self):
        """
        save new credentials to the credential lst
        """
        Credentials.credentials_list.append(
            self
        )

    def delete_credentials(self):
        """
        method to delete existing credentials
        """
        Credentials.credentials_list.remove(
            self
        )  # Using the remove() method to delete the user object from the user_list.

    @classmethod
    def find_credential(cls, account):
        """
        takes the account and return credentials that matches the account
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential


    @classmethod
    def if_credential_exist(cls, account):
        """
        sees if a credential exists from the credential list and returns a boolean.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        returns all credentials
        """
        return cls.credentials_list

    def generatePassword(stringLength=10):
        """
        Generates a random password
        """
        password = (
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + "~!@#$%^&*"
        )
        return "".join(random.choice(password) for n in range(stringLength))

####################
####################
######################
######################
######################
######################
######################
