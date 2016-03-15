#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 1 docstring."""


def get_matches(players):
    """List of versus matchups for players in a game.

    Args:
        players(list, str): A list of player names.

    Returns:
        matchups: List of versus matchups of players.

    Examples:

    >>> import task_01
    >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """
    matchups = []
    for i, player1 in enumerate(players):
        for j, player2 in enumerate(players):
            if i < j:
                matchups.append([player1, player2])
    return matchups
