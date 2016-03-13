#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1 file."""

NLIST = []


def get_matches(players):
    """To create a new list among the competitors.

    Args:
    players(list): the names of the competitors in a list.

    Returns:
    list: returns a new list among the competitors.

    Examples:

        >>> get_matches(['vim', 'sam', 'Mike'])
        '[('vim', 'sam'), ('vim', 'Mike'), ('sam', 'Mike')]'
    """
    for num, person1 in enumerate(players):
        for num2, person2 in enumerate(players):
            if num < num2:
                NLIST.append((person1, person2))
    return NLIST
