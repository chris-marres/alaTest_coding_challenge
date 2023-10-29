"""OperatorPriceEntry model test module."""

from models import OperatorPriceEntry


def test_operator_price_entry_comparison_operators():
    """Tests that the operator price entry class behaves exactly like a
    tuple in comparisons.
    """
    price1 = 0.1
    price2 = 0.2
    name1 = "name1"
    name2 = "name2"

    # Equal.
    assert OperatorPriceEntry(price1, name1) == OperatorPriceEntry(
        price1, name1
    )

    # Not equal.
    assert OperatorPriceEntry(price1, name1) != OperatorPriceEntry(
        price2, name1
    )
    assert OperatorPriceEntry(price1, name1) != OperatorPriceEntry(
        price1, name2
    )

    # Less than.
    assert OperatorPriceEntry(price1, name1) < OperatorPriceEntry(
        price2, name2
    )
    assert OperatorPriceEntry(price1, name1) < OperatorPriceEntry(
        price2, name1
    )
    assert OperatorPriceEntry(price1, name1) < OperatorPriceEntry(
        price1, name2
    )

    # If less than works, so does the greater than.
