from .exceptions import IBANValidationException
from .enums import BankEnum


class IBAN:
    cc: str = None
    cd: str = None
    bank: BankEnum = None
    account_type: str = None
    account_number: str = None

    character_map = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
    }

    def __init__(self, iban):
        self.cc, self.cd, self.bank, self.account_type, self.account_number = self.iban_parser(iban)

    @classmethod
    def iban_parser(cls, value):
        cc = value[:2]
        cd = value[2:4]
        bank = BankEnum.find_by_id(value[4:7])
        account_type = value[7]
        account_number = value[8:]
        return cc, cd, bank, account_type, account_number

    @classmethod
    def calculate_iban(cls, bank: BankEnum, value: str):
        cc = 'IR'
        cd = '00'
        bban = bank.id + '0' + f"{value:0>18}"
        t_iban = f'{cc}{cd}{bban}'
        tn_iban = cls(t_iban)
        cd = f'{(98 - int(tn_iban.to_number()) % 97):0>2}'
        return cls(f'{cc}{cd}{bban}')

    def to_number(self):
        new_value = f'{self.bank.id}{self.account_type}{self.account_number}'
        for item in self.cc:
            new_value = new_value + str(self.character_map[item])
        new_value = new_value + self.cd
        return new_value

    def __str__(self):
        return self.format(separator='')

    def format(self, separator=''):
        return f'{self.cc}{self.cd}{separator}{self.bank.id}{self.account_type}{separator}{self.account_number[:4]}{separator}{self.account_number[4:8]}{separator}{self.account_number[8:12]}{separator}{self.account_number[12:16]}{separator}{self.account_number[16:]}'

    def validate(self):
        try:
            value = self.__str__()
        except Exception:
            raise IBANValidationException()
        if len(value) != 26:
            raise IBANValidationException()
        new_value = IBAN(value).to_number()

        if len(new_value) != 28:
            raise IBANValidationException()

        if int(new_value) % 97 != 1:
            raise IBANValidationException
