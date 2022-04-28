class Credential:
    '''
    Class that generates new instances of account credentials
    '''
    def __init__(self,userId, account,first_name,last_name,phone_number,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            userId :id
            account: new account
            first_name: New credent first name.
            last_name : New credential last name.
            number: New credential phone number.
            email : New credential email address.
        '''
        self.userId = userId
        self.account = account
        self.first_name= first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password



    credential_list = [] #empty list


    
    def save_credential(self):
        '''Save new credential to credential_list'''

        Credential.credential_list.append(self)
    def delete_credential(self):
        '''delete a password-locker credential'''
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

        for credential in cls.credential_list:
            if credential.account == account:
                return credential

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
      

