#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""

import getpass
import authentication


def login(username, maxattempts=3):
    """ Defines a function to represent the login username and maximum number
    of attempts permitted.

    Args:
        username(str): A string representing the username
        maxattempts(int): An optional value representing the maximum number
        of prompted attempts

    Returns:
        True or false value depending on whether password is authenticated

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


    """

    authenticated = False
    numattempts = 0
    error = 'Incorrect username or password. You have {0} attempts left.'
    while authenticated is False and numattempts < maxattempts:
        password = getpass.getpass('Please ender your password:')

        if authentication.authenticate(username, password) is True:
            authenticated = True
        else:
            numattempts += 1
            print error.format(maxattempts - numattempts)

    return authenticated
