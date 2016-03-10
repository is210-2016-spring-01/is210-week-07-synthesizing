#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For loop to word counts of strings."""

import getpass
import authentication


def login(username, maxattempts=3):
    """A function to log a user in.

    Args:
        username (str), required: User's login name.
        maxattempts (int): Maximum number of login tries. Default = 3.

    Returns:
        bool: Whether a user has been successfully authenticated.

    Examples:
        >>> task_02.login('mike', 2)
        Please enter your password:
        Incorrect username of password. You have 1 attempts left.
        Please enter your password:
        Incorrect username of password. You have 0 attempts left.
        False

        >>> task_02.login('veruca', 2)
        Please enter your password:
        True
    """
    authenticated = False
    attempted = 0
    errormsg = 'Incorrect username of password. You have {0} attempts left.'
    while attempted < maxattempts and authenticated is False:
        password = getpass.getpass('Please enter your password:')
        authenticated = authentication.authenticate(username, password)
        attempted += 1
        if authenticated is False:
            print errormsg.format(maxattempts - attempted)
        else:
            return True
    return False
