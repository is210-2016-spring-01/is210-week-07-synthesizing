#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates a list of matchups for players in a tournament."""


def get_matches(players):
    """This docstring describes get matches.


    Args:
        players (list): A list of players.

    Returns:
        list: A new list of matchhups stored as a list of tuples.

    Examples
    >>> import data
    >>> print data
    >>> print data.VERSUS
    ['Fandral', 'Hogun', 'Volstagg', 'Sif', 'Amora', 'Lorelei',\
    'Balder', 'Frigga', 'Hermod', 'Gaea', 'Hoder', 'Tyr', 'Loki', \
    'Odin', 'Thor', 'Heimdall', 'Frey', 'Freya']
    >>> print get_matches(['Volstagg', 'Sif', 'Odin'])
    """
    matchups = []
    for playersa in enumerate(players):
        for playerb in enumerate(players):
            if playera[0] < playerb[0]:
                matchups.append((playera[1], playerb[1]))

    return matchups
