from azbankintro.exceptions import IBANValidationException
from azbankintro.utils import iban_to_number


def iban_validate(value):
    if len(value) != 26:
        raise IBANValidationException()
    new_value = iban_to_number(value)

    if len(value) != 28:
        raise IBANValidationException()

    if int(new_value) % 97 != 1:
        raise IBANValidationException
