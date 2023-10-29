"""PhoneNumber model test module."""

from models import PhoneNumber
from pytest import raises


def test_phone_number_validator():
    """Tests the validetion of a phone number on init."""
    # Phone number with 10 chars should not raise any errors.
    _ = PhoneNumber("1234567890")

    # Phone number with 9 chars should raise an error.
    with raises(ValueError):
        _ = PhoneNumber("123456789")
