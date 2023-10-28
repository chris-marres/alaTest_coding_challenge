"""Operator Price Entry Model."""


class OperatorPriceEntry(tuple):
    """Operator Price Entry Model."""

    def __new__(cls, price: float, operator_name: str):
        return super(OperatorPriceEntry, cls).__new__(
            cls, (price, operator_name)
        )

    def __init__(self, price: float, operator_name: str):
        self.price = price
        self.operator_name = operator_name

    def __reduce__(self):
        return (self.__class__, (self.price, self.operator_name))

    def __repr__(self) -> str:
        return (
            "OperatorPriceEntry"
            f'(price={self.price}, operator_name="{self.operator_name}")'
        )
