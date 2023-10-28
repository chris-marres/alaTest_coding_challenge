"""Peek Command."""

from models import OperatorPriceManager


def peek():
    """Peek into the stored price manager structure."""
    print(OperatorPriceManager())
