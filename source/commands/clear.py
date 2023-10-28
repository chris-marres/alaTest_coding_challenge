"""Clear Command."""

import os

import typer


def clear():
    """Clears the operator price manager state."""
    if os.path.exists("state/state.pkl"):
        os.system("rm state/state.pkl")
        typer.echo(typer.style("Stored state cleared.", fg=typer.colors.GREEN))
    else:
        typer.echo("Stored state is already empty.")
