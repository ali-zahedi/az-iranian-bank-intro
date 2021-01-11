__all__ = [
    'TextChoices', 'IntegerChoices', 'gettext_lazy',
    'card_validate', 'CardValidationException',
    'IBAN', 'iban_validate', 'IBANValidationException', 'BankDoesNotExistException',
    'BankEnum',
]


def _import_enum_local():
    from .utils import TextChoices as UTextChoices, IntegerChoices as UIntegerChoices
    return UTextChoices, UIntegerChoices


try:
    import django

    if django.__version__ >= '3.0':

        TextChoices = django.db.models.TextChoices
        IntegerChoices = django.db.models.IntegerChoices
    else:
        TextChoices, IntegerChoices = _import_enum_local()

    gettext_lazy = django.utils.translation.gettext_lazy
except ModuleNotFoundError:
    TextChoices, IntegerChoices = _import_enum_local()
    gettext_lazy = lambda x: x

from .validations import *
from .exceptions import *
from .enums import BankEnum
from .iban import IBAN
