"""Configuration/Helper file for the tests module."""

from models import OperatorPriceManager
from pytest import fixture


@fixture
def operator_price_manager() -> OperatorPriceManager:
    """OperatorPriceManager that auto resets after every test method."""
    yield OperatorPriceManager()
    OperatorPriceManager.reset_singleton()
