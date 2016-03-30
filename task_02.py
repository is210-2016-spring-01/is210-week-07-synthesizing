#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Passwords."""

import getpass
import authentication


def login(username, maxattempts=3):
    """login authenticates user to login.

    Args:
        username(str): enter username
        maxattempts(int, optional): The max number of prompted attempts.

    Returns:
        If true return true otherwise return false.

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

    authenticated = False
    attempt = 0
    warning = 'Incorrect username or password. You have {} attempts left.'

    while not authenticated and attempt < maxattempts:
        mypassd = getpass.getpass('Please enter your password:')

        if authentication.authenticate(username, mypassd) is True:
            authenticated = True

        else:
            attempt += 1
            print warning.format(maxattempts - attempt)
    return authenticated
