class IBANValidationException(Exception):
    """The IBAN did not validate"""

class BankDoesNotExistException(IBANValidationException):
    """The Bank does not exists"""
