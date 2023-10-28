"""Operator Price Manager Model."""

from pickle import dump, load
from pprint import pformat

from utils import SortedList

from .operator_price_entry import OperatorPriceEntry
from .phone_number import PhoneNumber
from .prefix_price_entry import PrefixPriceEntry


class OperatorPriceManager:
    """Operator Price Manager Model."""

    _instance = None  # Class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OperatorPriceManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            self.pricing_info: dict[str, SortedList] = {}
            self.longest_prefix = 0
            self.__initialized = True

    @classmethod
    def reset_singleton(cls):
        """Reset the Singleton instance to None."""
        cls._instance = None

    def store_state(self, filepath: str):
        with open(filepath, mode="wb") as file:
            dump(self, file)

    def load_state(self, filepath: str):
        with open(filepath, mode="rb") as file:
            loaded_state = load(file)
            self.pricing_info = loaded_state.pricing_info
            self.longest_prefix = loaded_state.longest_prefix

    def update_pricing_info(
        self,
        operator_name: str,
        prefix_price_entry_list: list[PrefixPriceEntry],
    ):
        for prefix, operator_price_list in self.pricing_info.items():
            entrys_to_remove = []

            for operator_price_entry in operator_price_list:
                if operator_price_entry.operator_name == operator_name:
                    entrys_to_remove.append(operator_price_entry)

            for entry in entrys_to_remove:
                operator_price_list.remove(entry)

            self.pricing_info[prefix] = operator_price_list

        for prefix_price_entry in prefix_price_entry_list:
            self.longest_prefix = max(
                self.longest_prefix,
                len(prefix_price_entry.prefix),
            )

            if prefix_price_entry.prefix not in self.pricing_info:
                self.pricing_info[prefix_price_entry.prefix] = SortedList()

            self.pricing_info[prefix_price_entry.prefix].append(
                OperatorPriceEntry(prefix_price_entry.price, operator_name)
            )

    def get_lowest_price_for_phone_number(
        self,
        phone_number: PhoneNumber,
    ) -> OperatorPriceEntry | None:
        found_list = None

        for prefix_lenth in range(self.longest_prefix, 0, -1):
            if found_list:
                break

            prefix = phone_number[0:prefix_lenth]
            found_list = self.pricing_info.get(prefix)

        return found_list[0] if found_list else found_list

    def __repr__(self):
        return (
            f"Longest prefix lenght: {self.longest_prefix}\n"
            f"Pricing Info:\n{pformat(self.pricing_info)}"
        )
