#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


import getpass
import authentication


def login(username, maxattempts=3):
    """Resembles the structure of a login or authentication screen.

    Args:
        username(str): Name of the user.
        maxattempts(int): Amount of password attempts with a default of 3.

    Returns:
        correct: Password is either True or False.

    Examples:

    >>> import task_02
    >>> task_02.login('mike', 4)
    Please enter your password:
    Incorrect username or password. You have 3 attempts left.
    Please enter your password:
    Incorrect username or password. You have 2 attempts left.
    Please enter your password:
    Incorrect username or password. You have 1 attempts left.
    Please enter your password:
    Incorrect username or password. You have 0 attempts left.
    False

    >>> import task_02
    >>> task_02.login('veruca', 2)
    Please enter your password:
    Incorrect username or password. You have 1 attempts left.
    Please enter your password:
    True
    """
    number_of_attempts = 0
    correct = False
    try_again = 'Incorrect username or password. You have {0} attempts left!'
    while not correct and number_of_attempts < maxattempts:
        ask_password = getpass.getpass('Please enter password:')
        if authentication.authenticate(username, ask_password) is True:
            correct = True
        else:
            number_of_attempts += 1
            print try_again.format(maxattempts - number_of_attempts)
    return correct
