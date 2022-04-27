#!/usr/bin/env python3.6
from credentials import Credential
from user import User

def create_user(first, last, phone, email, password):
    '''function for new user'''

    new_user = User(first, last, phone, email, password)
    return new_user


def save_user(user):
    '''Function to save new user'''

    user.save_user()


def delete_user(user):
    '''Function to delete user'''
    user.delete_user()


def find_user(number):
    '''function to find contact by number'''
    return User.find_by_number(number)


def display_users():
    '''function to return all account creds'''
    return User.display_users()

############
############



def create_cred(account,first_name,last_name, phone, email, password):
    '''function for new creds'''

    new_cred = Credential(account,first_name, last_name, phone, email, password)
    return new_cred
def save_cred(cred):
    '''Function to save new cred'''

    Credential.save_credential()
def delete_cred(user):
    '''Function to delete cred'''
    Credential.delete_credential()
def find_cred(account):
    '''function to find cred by account'''

    return Credential.find_by_number(account)
def display_users():
    '''function to return all accounts'''
    return Credential.display_credentials()
def check_register(number):
    return User.user_exists(number)



def main():
    save_user(create_user('yoshi','ahona','0743', 'hsh', 'fsi'))
    print("Hello, Welcome to PASSWORD LOCKER")
    username = input('What is your name?:')
    print(f'Hello {username}. What would you like to do?')


    print("Use these short codes : CA - create new account, LI - login to existing account")
    short_code = input()

    if short_code == 'ca':
        print("New Password locker account")
        print("-"*10)

        f_name = input("First Name:")
        l_name = input("Last Name:")
        phone = input('Phone number:')
        email = input('email address:')
        password = input('Create Password:')

        save_user(create_user(f_name, l_name, phone, email, password))
        

        print(f"New Password locker account {f_name} {l_name} created")

    elif short_code == 'li':

        pn = input("Enter your phone number:  ")

        if check_register(pn):
            the_user = find_user(pn)
            ps = input('Enter password')
            while the_user.password != ps:
                ps = input('enter the correct password')
            print(f'{the_user.first_name}')

            input(f'Hello {the_user.last_name}, What would you like to do? Reply with: ls-list accounts, na-new account, sa- search account  ')







        else:
            print('contact does not exist')
        #while check_register(pn)==False:
            #pn = input("Please Enter a registered number")
        #ps = input('Enter your password')
        #the_user = find_user(pn)

        

main()
    


