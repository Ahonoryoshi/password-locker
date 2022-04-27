#!/usr/bin/env python3.6
from user import User

def create_user(first, last, phone, email, password):
    '''function for new user'''

    new_user = User(first, last, phone, email, password)
def save_user(user):
    '''Function to save new user'''
    user.save_user()