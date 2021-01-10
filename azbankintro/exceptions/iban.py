class IBANValidationException(Exception):
    """The IBAN did not validate"""

class BankDoesNotExistException(Exception):
    """The Bank does not exists"""
