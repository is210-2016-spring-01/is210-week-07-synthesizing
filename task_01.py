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
    for i in enumerate(players):
        # ...compute some result based on item ...
        print i
