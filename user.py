
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


class Credentials:
    """
    Class to create account instances
    """

    credentials_list = []

    @classmethod
    def verify_user(cls, username, phone_number, password):
        """
        checks for registered users
        """
        myuser = ""
        for user in User.user_list:
            if user.username == username and user.password == password and user.phone_number == phone_number:
                myuser == user.username
        return myuser

    def __init__(self, account, username,phone_number, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = username
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
        method that takes the account_name and return credentials that matches the account
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def copy_password(cls, account):
        """
        method that takes allows copying and pasting a credential
        """
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(
            found_credentials.password
        )  # pyperclip.copy() method allows us to copy passed in items to the machines clipboard

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list

    def generatePassword(stringLength=8):
        """
        Generate a random password string of letters and digits and special characters
        """
        password = (
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + "~!@#$%^&*"
        )
        return "".join(random.choice(password) for i in range(stringLength))

    def create_new_user(username, password):
        """
        Function to create a new user with a username and password
        """
        new_user = User(username, password)
        return new_user

    def save_user(user):
        """
        Function to save a new user
        """
        user.save_user()

    def display_user():
        """
        Function to display existing user
        """
        return User.display_user()

    def login_user(username, password):
        """
        function that checks whether a user exist and then login the user in.
        """

        check_user = Credentials.verify_user(username, password)
        return check_user

    def create_new_credential(account, userName, password):
        """
        Function that creates new credentials for a given user account
        """
        new_credential = Credentials(account, userName, password)
        return new_credential

    def save_credentials(credentials):
        """
        Function to save Credentials to the credentials list
        """
        credentials.save_details()

    def display_accounts_details():
        """
        Function that returns all the saved credential.
        """
        return Credentials.display_credentials()

    def delete_credential(credentials):
        """
        Function to delete a Credentials from credentials list
        """
        credentials.delete_credentials()

    def find_credential(account):
        """
        Function that finds a Credentials by an account name and returns the Credentials that belong to that account
        """
        return Credentials.find_credential(account)

    def check_credendtials(account):
        """
        Function that check if a Credentials exists with that account name and return true or false
        """
        return Credentials.if_credential_exist(account)

    def generate_Password():
        """
        generates a random password for the user.
        """
        auto_password = Credentials.generatePassword()
        return auto_password

    def copy_password(account):
        """
        A funct that copies the password using the pyperclip framework
        We import the framework then declare a function that copies the emails.
        """
        return Credentials.copy_password(account)