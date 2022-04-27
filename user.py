#from operator import truediv


class User:
    '''
    Class that generates new instances of users
    '''
    def __init__(self,first_name,last_name,phone_number,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New User first first_name.
            last_name : New User last last_name.
            number: New contact phone number.
            email : New contact email address.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
    user_list = [] #empty list
    def save_user(self):
        '''Save new user to user_list'''

        self.user_list.append(self)
    def delete_user(self):
        '''delete a password-locker user'''
        self.user_list.remove(self)

    @classmethod
    def user_exists(cls,number):
        '''Function that checks if a user is regestered'''
        for user in cls.user_list:
            if user.phone_number == number:
                return True
            else:
                return False


    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a User that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
      

