#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a loop"""

import getpass
import authentication


def login(username, maxattempts=3):
    """A function that logins in with username and password.

    Args:
        username(str): Insert username here to login
        maxattempts(int, optional): Max attempts before False. Default = 3.

    Returns:
        bool: True or False, depending on auntheication.

    Examples:

        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorret username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password: YOu have 0 attempts left.

        >>> task_02.login('veruca', '2')
        Please enter your password:
        True
    """

    authenticated = False
    attempted = 0
    errormsg = 'Incorrect username or password. You have {0} attempts left.'
    while attempted < maxattempts and authenticated is False:
        password = getpass.getpass('Please enter your password:')
        authenticated = authentication.authenticate(username, password)
        attempted += 1
        if authenticated is False:
            print errormsg.format(maxattempts - attempted)
        else:
            return True
        return False
