#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 7 synthesizing task with a login simulation function"""

import getpass
from authentication import authenticate as authcheck


def login(username, maxattempts=3):
    """Prompts for the users password and attempts (maxattempts) to authenticate
       the login request

    Args:
        username (str): the name of the user attempting login.
        maxattempts (int): the maximum number of login attempts

    Returns:
        boolean: an indicater of the login success (True) or not (False)

    Examples:
        >>> login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        >>> login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        True
    """

    logged_in = False

    while not logged_in and maxattempts:

        logged_in = authcheck(username,
                              getpass.getpass('Please enter your password: '))

        if not logged_in:

            maxattempts -= 1
            print 'Incorrect username or password. ' + \
                  'You have {0} attempts left.'.format(maxattempts)

    return logged_in
