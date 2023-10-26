"""Phone Number Model."""


class PhoneNumber(str):
    """Phone Number Model."""

    def __new__(cls, value):
        if len(value) < 10:
            raise ValueError(
                "PhoneNumber length must be at least 10 characters long."
            )

        return super(PhoneNumber, cls).__new__(cls, value)
