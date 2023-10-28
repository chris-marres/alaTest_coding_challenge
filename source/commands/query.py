"""Query Command."""

import sys

import typer
from models import OperatorPriceManager, PhoneNumber


def query(phone_number: str):
    """Query the price manager for the best price, given a phone
    number.
    """
    try:
        phone_number = PhoneNumber(phone_number)
    except ValueError as e:
        typer.echo(typer.style(e, fg=typer.colors.RED))
        return

    operator_price_manager = OperatorPriceManager()

    result = operator_price_manager.get_lowest_price_for_phone_number(
        phone_number
    )

    if result:
        message = (
            f"The best price is {result.price}"
            f" from the operator {result.operator_name}."
        )
        typer.echo(typer.style(message, fg=typer.colors.GREEN))
    else:
        message = "There is no prefix matching the phone number provided."
        typer.echo(typer.style(message, fg=typer.colors.RED))
