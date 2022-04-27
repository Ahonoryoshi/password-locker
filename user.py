class User:
    '''
    Class that generates new instances of users
    '''
    def __init__(self,first_name,last_name,phone_number,email,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New User first name.
            last_name : New User last name.
            number: New contact phone number.
            email : New contact email address.
        '''
        self.first = first_name
        self.last = last_name
        self.number = phone_number
        self.email = email
        self.password = password
    user_list = [] #empty list
    def save_user(self):
        '''Save new user to user_list'''

        User.user_list.append(self)
    def delete_user(self):
        '''delete a password-locker user'''
        User.user_list.remove(self)
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
      

