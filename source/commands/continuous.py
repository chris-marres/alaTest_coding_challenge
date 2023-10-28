"""Continuous Command."""

import sys

from .query import query


def continuous():
    """Starts a session where multiple queries can be executed one
    after the other.
    """
    print("A querying session has started. To exit press EOF(Ctrl+D).")
    for line in sys.stdin:
        query(line.strip())
