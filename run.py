#!/usr/bin/env python3.6
from collections import UserList
from credentials import Credential
from user import User

def create_user(first, last, phone, email, password):
    '''function for new user'''

    new_user = User(first, last, phone, email, password)
    return new_user


def save_user(user):
    '''Function to save new user'''

    User.user_list.append(user)

def delete_user(user):
    '''Function to delete user'''
    user.delete_user()


def find_user(number):
    '''function to find contact by number'''
    return User.find_by_number(number)


def display_users():
    '''function to return all account creds'''
    return User.display_users()
def check_register(number):
    return User.user_exists(number)

############
############

the_list = []

def create_cred(userId, account,first_name,last_name, phone, email, password):
    '''function for new creds'''

    new_cred = Credential(userId,account,first_name, last_name, phone, email, password)
    return new_cred
def save_cred(cred):
    '''Function to save new cred'''

    cred.save_credential()
def delete_cred(user):
    '''Function to delete cred'''
    Credential.delete_credential()
def find_cred(account):
    '''function to find cred by account'''

    return Credential.find_by_number(account)
def display_creds():
    '''function to return all accounts'''
    return Credential.display_credentials()



def main():
    while True:
        save_cred(create_cred(123,'instagram','ahona', 'john','0743','fsfs','qwerty'))
        #save_cred(123,'facebook', 'ahonoryoshi', 'jy', '0743088648','asdf','pqrs' )
        
        save_user(create_user('yoshi','ahona','0743', 'hsh', 'fsi'))
        print("Hello, Welcome to PASSWORD LOCKER")
        username = input('What is your name?:')
        print(f'Hello {username}. What would you like to do?')


        print("Use these short codes")
        print('CA - create new account')
        print('LI - login to existing account')
        short_code = input('.....')

        if short_code == 'ca':
            print("New Password locker account")
            print("-"*10)
            f_name = input("First Name:")
            l_name = input("Last Name:")
            phone = input('Phone number:')
            email = input('email address:')
            password = input('Create Password:')

            new = create_user(f_name, l_name, phone, email, password)
            save_user(new)

            User.user_list.append(new)

            print(User.user_list)
            

            print(f"New Password locker account {f_name} {l_name}  created")
            
            

        elif short_code == 'li':

            pn = input("Enter your phone number:  ")

            if check_register(pn):
                the_user = find_user(pn)
                ps = input('Enter password')
                while the_user.password != ps:
                    ps = input('enter the correct password')
                print(f'{the_user.first_name}')

                print(f'Hello {the_user.last_name}, What would you like to do? Reply with:')
                print('ls-list accounts')
                print('na-new account')
                print('sa- search account')
                print('da- delete-account')
                short = input('')

                if short == 'ls':

                    print('ls')
                    if display_creds():
                        print("Here is a list of all your accounts")
                        print('\n')

                        for cred in display_creds():
                            print(f"{cred.account} {cred.last_name} .....{cred.phone_number}")

                            print('\n')
                    else:
                        print('\n')
                        print("You dont seem to have any accounts saved yet")
                        print('\n')


                elif short == 'na':
                    userId = input('Enter your user id')
                    print('na')
                    acc = input('account')
                    first = input("First Name:")
                    last = input("Last Name:")
                    n = input('Phone number:')
                    em = input('email address:')
                    pas = input('Create Password:')
                    

                    save_cred(create_cred(userId,acc,first,last,n, em, pas))
                elif short == 'da':
                    if display_creds():
                        print("Here is a list of all your accounts")
                        print('which one do you want to delete?')
                        print('\n')

                        for cred in display_creds():
                            print(f"{cred.account} {cred.last_name} .....{cred.phone_number}")

                            print('\n')
                        

                    else:
                        print('\n')
                        print("You dont seem to have any accounts saved yet")
                        print('\n')

                    
                    
                
                    

                else:
                    print('search')

                







            else:
                print('contact does not exist')
            #while check_register(pn)==False:
                #pn = input("Please Enter a registered number")
            #ps = input('Enter your password')
            #the_user = find_user(pn)

        

main()
    


