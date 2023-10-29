"""Main entry point for the CLI application."""

import os

import typer
from commands import clear, continuous, peek, query, test, update
from models import OperatorPriceManager

app = typer.Typer(add_completion=False)
app.command()(peek)
app.command()(query)
app.command()(update)
app.command()(continuous)
app.command()(clear)
app.command()(test)


if __name__ == "__main__":
    operator_price_manager = OperatorPriceManager()

    if not os.path.exists("state"):
        os.makedirs("state")
    else:
        if os.path.exists("state/state.pkl"):
            operator_price_manager.load_state("state/state.pkl")

    app()
