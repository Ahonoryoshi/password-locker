
from user import User
from creds import Credentials


def create_new_user(username,phone_number, password):
    """
    Function to create a new user with a username and password
    """
    new_user = User(username,phone_number, password)
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


def login_user(username, phone_number, password):
    """
    function to check if a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username,phone_number, password)
    return check_user


def create_new_credential(account, userName, phone_number, password):
    """
    Function to create new credentials for a user account
    """
    new_credential = Credentials(account, userName,phone_number, password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_details()


def display_accounts_details():
    """
    Function to display all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function to find a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)


def generate_Password():
    """
    function to generate a random password for the user.
    """
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):
    """
    function to copy the password using the pyperclip
    """
    return Credentials.copy_password(account)


def main():
    save_user(create_new_user('Ahonoryoshi','0743088648', 'yoshi@12548?'))





    print(
        "Hello and  Welcome to Password Locker...\n select one of the short codes below to proceed:\n CA --->  To Create New Account  \n LI --->  To Log in to existing account  \n"
    )
    short_code = input("").lower().strip()


    if short_code == "ca":
        print("Register here:")
        print("*" * 20)
        username = input("User_name: ")

        phone_number = input('phone number:')
        while True:
            print(" click :  CP <--> To type your own pasword:\n GP <--> To generate random Password")
            password_opt= input().lower().strip()
            if password_opt == "cp":
                password = input("Enter Password\n")
                break
            elif password_opt == "gp":
                password = generate_Password()
                break
            else:
                print("Invalid option please try again")


        save_user(create_new_user(username,phone_number, password))
        print("*" * 40)
        print(
            f"Hello {username}, Your account has been created succesfully! Your password is: {password}"
        )
        print("*" * 40)



    elif short_code == "li":
        print("*" * 40)
        print("Enter your User name, phone number, and your Password to log in:")
        print("*" * 40)
        username = input("Username: ")
        phone_number = input("Phone Number:")
        password = input("password: ")
        login = login_user(username, phone_number, password)

        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker")
            print("\n")

    
    while True:
        print(
            "Use these short codes:\n CC - Create a new account credential \n DC - Display saved Credentials \n FC - Find an account's credentials \n DEL - Delete a credential \n EX - Exit password locker \n"
        )
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create new account credentials")
            print("." * 20)
            print("Account name :")
            account = input().lower()
            phone = input('Phone_number')
            print("Your Account username")
            username = input()
            while True:
                print(
                    " CP - To type your own password if you already have an account:\n GP - To generate random Password"
                )
                password_Choice = input().lower().strip()
                if password_Choice == "cp":
                    password = input("Type your password\n")
                    break
                elif password_Choice == "gp":
                    password = generate_Password()
                    break
                else:
                    print("Invalid option please try again")
            save_credentials(create_new_credential(account, username,phone, password))
            print("\n")
            print(
                f"Account Credential for: {account} - UserName: {username} - Password:{password} created succesfully"
            )
            print("\n")
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acounts: ")

                print("*" * 80)
                print("_" * 40)
                for account in display_accounts_details():
                    print(
                        f" Account:{account.account} \n phone Number:{account.phone_number}\n User Name:{username}\n Password:{password}"
                    )
                    print("_" * 40)
                print("*" * 40)
            else:
                print("No such account found:(")
        elif short_code == "fc":
            print("Enter the Account Name you are searching for:")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print("-" * 50)
                print(f"User Name: {search_credential.username}")
                print(f"Phone : {search_credential.phone_number}")
                print( f"Password :{search_credential.password}")
                print("-" * 50)
            else:
                print("The account Credential does not exist")
                print("\n")
        elif short_code == "del":
            print("Enter the account name for the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_" * 40)
                search_credential.delete_credentials()
                print("\n")
                print(f"Your credentials for : {search_credential.account} has been deleted successfully")
                print("\n")
            else:
                print(
                    "Account inexistent"
                )

        elif short_code == "gp":

            password = generate_Password()
            print(
                f" your password is  {password}"
            )
        elif short_code == "ex":
            print("Thanks for using password-locker! Hope to see you soon")
            break
        else:
            print("Wrong entry... Check your entry and retry")
    else:
        print('Enter a valid input')


if __name__ == "__main__":
    main()