#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Player Matches"""


def get_matches(players):
    """get_matches matches players.

    Arg:
       players(str): list of names.

    Returns:
        Returns tuple = a group created matches

    Examples:
        >>> get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """

    player = []
    lists = list(enumerate(players))
    for frst in lists:
        for scnd in lists:
            if frst[0] < scnd[0]:
                player.append((frst[1], scnd[1]))
    return player
