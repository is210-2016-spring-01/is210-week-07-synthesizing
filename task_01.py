#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a loop"""


def get_matches(players):
    """A function that returns player matchups using a list.

    Args:
        players (list, required): List of player names.

    Returns:
        tuples: Several tuple strings resulted in matchups.

    Examples:

        >>> get_matches(['Knicks', 'Cavaliers', 'Raptors'])
        [('Knicks', 'Cavaliers'), ('Knicks', 'Raptors'),
        ('Cavaliers', 'Raptors')]

        >>> get_matches(['Giants, 'Jets', 'Patriots'])
        [('Giants, 'Jets'), ('Giants', 'Patriots'),
        ('Jets', 'Patriots')]
    """

    games = []
    for team1 in enumerate(players):
        for team2 in enumerate(players):
            if team1[0] < team2[0]:
                games.append((team1[1], team2[1]))

    return games
