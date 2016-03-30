#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Half Cartesian function."""


def get_matches(players):
    """Creates unique player matches .

    Args:
        players (list): A list of players.

    Returns:
        tuples: List of matched players.

    Examples:
        >>> get_matches(['Ze', 'Two', 'Tank'])
        [('Ze', 'Two'), ('Ze', 'Tank'), ('Two', 'Tank')]
        >>> get_matches(['Man', 'Boy', 'Girl', 'Woman'])
        [('Man', 'Boy'), ('Man', 'Girl'), ('Man', 'Woman'),
        ('Boy', 'Girl'), ('Boy', 'Woman'), ('Girl', 'Woman')]
    """
    matches = []
    playersdup = players
    for num, oppon in enumerate(players):
        for numdup, oppondup in enumerate(playersdup):
            if num < numdup:
                matches.append((oppon, oppondup))
            else:
                continue
    return matches
