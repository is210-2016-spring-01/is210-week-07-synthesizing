#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2 file."""

import getpass
import authentication


def login(username, maxattempts=3):
    """To verify one's account ID and password.

    Args:
    username(str): input username.
    maxattempts(int): maximum attempts allowed.

    Returns:
    Bool: to return whether if someone entered the matching value, in boolen.

    Examples:

        >>>task_02.login('mike', 2)
        'Please enter your password:
         Incorrect username of password. You have 1 attempts left.
         Please enter your password:
         Incorrect username of password. You have 0 attempts left.
         False'
    """
    authenticated = False
    attempts = 0
    fail_message = 'Incorrect username or password. You have {0} attempts left.'
    while attempts < maxattempts and authenticated is False:
        password = getpass.getpass('Please enter your password: ')
        info = authentication.authenticate(username, password)
        attempts += 1
        if authenticated is False:
            print fail_message.format(maxattempts - attempts)
        else:
            return True
    return authenticated
