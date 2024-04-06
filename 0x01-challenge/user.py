#!/usr/bin/python3
"""
User class
"""


class User():
    """ class that defines a user """

    def __init__(self):
        """ initialization method for the user class """
        self.__email = None

    @property
    def email(self):
        """ property setter for the email attribute"""
        return self.__email

    @email.setter
    def email(self, value):
        """ setter for the email attribute"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
