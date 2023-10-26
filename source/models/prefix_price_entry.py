"""Prefix Price Entry Model."""


class PrefixPriceEntry:
    """Prefix Price Entry Model."""

    def __init__(self, prefix: str, price: float):
        self.prefix = prefix
        self.price = price

    def __repr__(self) -> str:
        return f"PrefixPriceEntry(prefix={self.prefix}, price={self.price})"
