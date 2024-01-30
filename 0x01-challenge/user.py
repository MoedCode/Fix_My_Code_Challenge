#!/usr/bin/python3
"""
User class
"""


class User():
    """ user class """

    __email = None

    def __init__(self):
        """ init method """
        self.__email = None

    @property
    def email(self):
        """ gets an email """
        return self.__email

    @email.setter
    def email(self, value):
        """ sets an email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
