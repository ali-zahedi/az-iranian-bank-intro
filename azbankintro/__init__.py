__all__ = [
    'TextChoices', 'IntegerChoices', 'gettext_lazy',
    'card_validate', 'CardValidationException',
    'iban_to_number', 'iban_parser', 'iban_validate', 'IBANValidationException',
    'BankEnum',
]


def _import_enum_local():
    from .utils import TextChoices as UTextChoices, IntegerChoices as UIntegerChoices
    return UTextChoices, UIntegerChoices


try:
    import django

    if django.__version__ >= '3.0':

        TextChoices = django.models.TextChoices
        IntegerChoices = django.models.IntegerChoices
    else:
        TextChoices, IntegerChoices = _import_enum_local()

    gettext_lazy = django.utils.translation.gettext_lazy
except ModuleNotFoundError:
    TextChoices, IntegerChoices = _import_enum_local()
    gettext_lazy = lambda x: x

from .validations import *
from .exceptions import *
from .enums import BankEnum
from .utils import iban_parser, iban_to_number
