class Credential:
    '''
    Class that generates new instances of account credentials
    '''
    def __init__(self,account,first_name,last_name,phone_number,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:

            account: new account
            first_name: New User first name.
            last_name : New User last name.
            number: New contact phone number.
            email : New contact email address.
        '''
        self.account = account
        self.first = first_name
        self.last = last_name
        self.number = phone_number
        self.email = email
        self.password = password
    credential_list = [] #empty list
    def save_user(self):
        '''Save new user to credential_list'''

        Credential.credential_list.append(self)
    def delete_credential(self):
        '''delete a password-locker user'''
        Credential.credential_list.remove(self)
    @classmethod
    def find_by_number(cls,account):
        '''
        Method that takes in a number and returns credentials that matches that account.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.account == account:
                return user

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
      

