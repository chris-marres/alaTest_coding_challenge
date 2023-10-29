"""Test Command."""

import os


def test():
    """Runs the tests."""
    os.system("cd source && python -m pytest --no-header -vs")
