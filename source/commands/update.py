"""Update Command."""

import sys
from csv import DictReader
from pathlib import Path

import typer
from models import OperatorPriceManager, PrefixPriceEntry
from typing_extensions import Annotated


def path_exists(path: str, message: str):
    """Check if a path exists and print a message if it doesn't."""
    if not Path(path).exists():
        typer.echo(typer.style(message, fg=typer.colors.RED))
        sys.exit(1)


def validate_file(filepath: str):
    """Check that the format of the csv file is correct."""
    with open(filepath, encoding="utf-8", mode="r") as file:
        if file.readline().strip() != "prefix;price_per_minute":
            typer.echo(
                typer.style("Invalid file headers", fg=typer.colors.RED)
            )
            sys.exit(1)


def read_price_catalog_file(filepath: str) -> list[PrefixPriceEntry]:
    with open(filepath, encoding="utf-8", mode="r") as file:
        price_catalog = DictReader(file, delimiter=";")

        return [
            PrefixPriceEntry(
                price_entry["prefix"], price_entry["price_per_minute"]
            )
            for price_entry in price_catalog
        ]


def update(
    operator_name: str,
    csv_filepath: Annotated[
        Path,
        typer.Argument(
            help=(
                "Specify a csv file that contains the pricing list of an"
                " operator that will be used to update the price manager data"
                " stracture."
            ),
        ),
    ],
):
    """Updates the price manager data structure."""
    path_exists(csv_filepath, "File not found.")
    validate_file(csv_filepath)

    operator_price_manager = OperatorPriceManager()

    operator_price_catalog = read_price_catalog_file(csv_filepath)
    operator_price_manager.update_pricing_info(
        operator_name,
        operator_price_catalog,
    )

    operator_price_manager.store_state("state/state.pkl")
