#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Return a list of unique matchups based on inputted player names."""


def get_matches(players):
    """A function to find unique matches between opponents.

    Args:
        players (list), required: Inputted string or list of player names.

    Returns:
        list of tuples: Tuples showing unique matches in a list.

    Examples:
        >>> get_matches(['Howard', 'Fred', 'Gary', 'JD'])
        [('Howard', 'Fred'), ('Howard', 'Gary'), ('Howard', 'JD'),
        ('Fred', 'Gary'), ('Fred', 'JD'), ('Gary', 'JD')]

        >>> get_matches(['Rangers', 'Islanders', 'Devils'])
        [('Rangers', 'Islanders'), ('Rangers', 'Devils'),
        ('Islanders', 'Devils')]
    """
    matchups = []
    for player1 in enumerate(players):
        for player2 in enumerate(players):
            if player1[0] < player2[0]:
                matchups.append((player1[1], player2[1]))

    return matchups
