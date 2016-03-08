#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates a list of matchups for players in a tournament."""


def get_matches(players):
    """This docstring describes get matches.

    Args:
        players (list): A list of players.

    Returns:
        list: A newly created list of tuples

    Examples
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """
    task_01.get_matches([',', ',', ','])
    list(enumerate(players))
    for item in players:
        print item
