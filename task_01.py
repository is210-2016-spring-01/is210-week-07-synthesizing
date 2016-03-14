#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Matches people together"""


def get_matches(players):
    """pairs people together, doesn't repeat pairs.

    Args:
        players(str): list of names

    Returns:
        tuple: players grouped together

    Examples:
        >>>task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]


    """
    group = []
    people = list(enumerate(players))
    for persona in people:
        for personb in people:
            if persona[0] < personb[0]:
                group.append((persona[1], personb[1]))
    return group
