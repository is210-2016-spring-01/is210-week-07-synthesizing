#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Password stuff happens here!"""

import getpass
import authentication


def login(username, maxattempts=3):
    """Lets the user in if the password is correct.

    Args:
        username (str): user inputs username
        maxattempts (int, optional): max number of allowed attempts

    Returns:
        Returns a boolean value of true or false based on if U/P are correct.

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

    """
    attempt = 0
    failiure = 'Incorrect username/password. You have {} attempts left!'
    authenticated = False
    while not authenticated and attempt < maxattempts:
        enter = getpass.getpass('Please enter password')
        if authentication.authenticate(username, enter) is True:
            authenticated = True
        else:
            attempt += 1
            print failiure.format(maxattempts - attempt)
    return authenticated
