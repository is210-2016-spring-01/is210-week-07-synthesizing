#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 7 synthesizing task with a player matching function"""


def get_matches(players):
    """Produce a list of tuples defining all the potential player matches

    Args:
        players (list): the list of all the player names.

    Returns:
        list: contains the list of possible player matches in the form of
              tuples with each tuple being the two player names

    Examples:
        >>> get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """

    match_list = []

    for plyrnum, plyrname in enumerate(players[:-1]):

        for plyr2 in players[plyrnum + 1:]:

            match_list.append((plyrname, plyr2))

    return match_list
