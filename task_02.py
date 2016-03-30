#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring creates a loop to word counts of strings."""

import authentication
import getpass


def login(username, maxattempts=3):
    """This function creates a login.


    Args:
        username (str): A user's login name.
        maxattempts (int): The maximum tries allowed. Default = 3.

    Returns:
        bool: Whether or not a user has been authenticated.

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
    authenticated = False
    attempted = 0
    errormessage = 'Incorrect username or password. You have {0} attempts left.'
    while attempted < maxattempts and authenticated is False:
        password = getpass.getpass('Please enter your password:')
        authenticated = authentication.authenticate(username, password)
        attempted += 1
        if authenticated is False:
            print errormessage.format(maxattempts - attempted)
        else:
            return True
    return False
