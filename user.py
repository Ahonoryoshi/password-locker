class User:
    '''
    Class that generates new instances of users
    '''
    def __init__(self,first_name,last_name,phone_number,email):

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
       
