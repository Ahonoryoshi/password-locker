#!/usr/bin/env python3.6
from user import User

def create_user(first, last, phone, email, password):
    '''function for new user'''

    new_user = User(first, last, phone, email, password)
def save_user(user):
    '''Function to save new user'''

    User.save_user()
def delete_user(user):
    '''Function to delete user'''
    User.delete_user()
def find_contact(number):
    '''function to find contact by number'''

    return User.find_by_number(number)
def display_users():
    '''function to return all accounts'''
    return User.display_users()


def main()
