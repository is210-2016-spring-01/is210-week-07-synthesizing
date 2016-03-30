#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Authentication module."""

import getpass
import authentication


def login(username, maxattempts=3):
    """Login module.

    Args:
        username (str): Name of user.
        maxattempts (int, optional): Max number of attempts, defaults to 3.

    Returns:
        bool: Whether login is successful or not (True/False).

    Examples:
        >>> task_02.login('violet', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        >>> task_02.login('mike', )
        Please enter your password:
        True
    """
    auth = False
    wrong = 'Incorrect username or password. You have {0} attempts left.'
    while auth is False and maxattempts > 0:
        password = getpass.getpass('Please enter your password: ')
        auth = authentication.authenticate(username, password)
        if auth is False:
            maxattempts -= 1
            print wrong.format(maxattempts)
    return auth
