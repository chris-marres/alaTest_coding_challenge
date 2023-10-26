from csv import DictReader

from models import OperatorPriceManager, PhoneNumber, PrefixPriceEntry


def read_price_catalog_file(filepath: str) -> list[PrefixPriceEntry]:
    with open(filepath, encoding="utf-8") as file:
        price_catalog = DictReader(file, delimiter=";")

        return [
            PrefixPriceEntry(
                price_entry["prefix"], price_entry["price_per_minute"]
            )
            for price_entry in price_catalog
        ]


if __name__ == "__main__":
    operator_price_manager = OperatorPriceManager()

    operator_a_price_catalog = read_price_catalog_file(
        "data/price_lists/operator_a.csv"
    )

    operator_price_manager.update_pricing_info(
        "Operator A", operator_a_price_catalog
    )

    operator_b_price_catalog = read_price_catalog_file(
        "data/price_lists/operator_b.csv"
    )

    operator_price_manager.update_pricing_info(
        "Operator B", operator_b_price_catalog
    )

    try:
        phone_number = PhoneNumber("4673867890")
    except ValueError as e:
        print(f"Error: {e}")
        exit()

    result = operator_price_manager.get_lowest_price_for_phone_number(
        phone_number
    )

    print(result)
