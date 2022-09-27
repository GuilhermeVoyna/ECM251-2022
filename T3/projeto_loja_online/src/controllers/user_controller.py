from tkinter.font import names
from unicodedata import name
import streamlit as st
from src.models.user import User

from pathlib import Path

import streamlit_authenticator as stauth


class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
            User(name="Joao",username="ratin0", password = "123", email = "damian@wayneenterprises.com"),
            User(name="Fausto",username="batman", password = "456", email = "joao2@gmail.com"),
            User(name="ADM",username="adm", password = "adm", email = "joao2@gmail.com")
        ]
    
    def check_user(self,user):
        return user in self.users

    def get_passwords(self):
        passwords=[]
        for user in self.users:
            val = user.get_password()
            passwords.append(val)
        return passwords
    def get_usernames(self):
        usernames=[]
        for user in self.users:
            val = user.get_username()
            usernames.append(val)
        return usernames
    def get_names(self):
        names=[]
        for user in self.users:
            val = user.get_name()
            names.append(val)
        return names
    def get_emails(self):
        vec=[]
        for user in self.users:
            val = user.get_email()
            vec.append(val)
        return vec                 