#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""


def get_matches(players):
    """Defines a function that produces a list of unique matchups

    Args:
        players(list): A list of player names

    Returns:
        tuple: unique matchups between players

    Examples:
    >>> import task_01
    >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')

    """

    matches = []
    for player1 in enumerate(players):
        for player2 in enumerate(players):
            if player1[0] < player2[0]:
                matches.append((player1[1], player2[1]))
    return matches
