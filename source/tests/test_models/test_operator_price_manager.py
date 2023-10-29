"""OperatorPriceManager model test module."""

from random import choices, randint
from string import digits

from conftest import operator_price_manager
from models import (
    OperatorPriceEntry,
    OperatorPriceManager,
    PhoneNumber,
    PrefixPriceEntry,
)


def test_singleton_pattern():
    """Tests that the operator price manager class works as a
    singleton.
    """
    instanse1 = OperatorPriceManager()
    instanse1.pricing_info = {"test_key": "test_value"}

    instanse2 = OperatorPriceManager()

    assert instanse1 == instanse2
    assert instanse1.pricing_info == instanse2.pricing_info
    assert instanse1 is instanse2

    # Reset singleton.
    OperatorPriceManager.reset_singleton()

    instanse3 = OperatorPriceManager()
    assert instanse1 is not instanse3


def test_no_duplicate_entrys_for_the_same_operator(operator_price_manager):
    """Tests that the operator price manager data structure works as
    expected.
    """
    prefix_price_entry_list = [PrefixPriceEntry("44", "0.1")]

    operator_price_manager.update_pricing_info(
        "Operator A", prefix_price_entry_list
    )
    operator_price_manager.update_pricing_info(
        "Operator A", prefix_price_entry_list
    )

    assert len(operator_price_manager.pricing_info["44"]) == 1


def test_sorted_lists_are_actually_sorted(operator_price_manager):
    """Tests that the sorted lists in the data structure are actually
    sorted.
    """
    operator_price_manager.update_pricing_info(
        "Operator A", [PrefixPriceEntry("44", 0.2)]
    )

    operator_price_manager.update_pricing_info(
        "Operator B", [PrefixPriceEntry("44", 0.1)]
    )

    operator_price_manager.update_pricing_info(
        "Operator C", [PrefixPriceEntry("44", 0.1)]
    )

    assert operator_price_manager.pricing_info["44"] == [
        OperatorPriceEntry(0.1, "Operator B"),
        OperatorPriceEntry(0.1, "Operator C"),
        OperatorPriceEntry(0.2, "Operator A"),
    ]


def test_operator_price_manager_returns_correct_result(operator_price_manager):
    """Tests that the operator price manager returns the correct
    result given some queries.
    """
    low_price, high_price = sorted(
        (randint(1, 100) / 100, randint(1, 100) / 100)
    )

    low_price_operator_name = "Cheap Operator"
    hight_price_operator_name = "Expensive Operator"

    prefixes = ["".join(choices(digits, k=randint(1, 5))) for _ in range(10)]

    operator_price_manager.update_pricing_info(
        low_price_operator_name,
        [
            PrefixPriceEntry(prefix, price)
            for prefix, price in zip(
                prefixes, [low_price for _ in range(len(prefixes))]
            )
        ],
    )

    operator_price_manager.update_pricing_info(
        hight_price_operator_name,
        [
            PrefixPriceEntry(prefix, price)
            for prefix, price in zip(
                prefixes, [high_price for _ in range(len(prefixes))]
            )
        ],
    )

    for prefix in prefixes:
        assert operator_price_manager.get_lowest_price_for_phone_number(
            PhoneNumber(prefix + "1234567890")
        ) == OperatorPriceEntry(low_price, low_price_operator_name)
