from types import DynamicClassAttribute

from azbankintro import TextChoices, gettext_lazy as _
from .exceptions import BankDoesNotExistException


class BankEnum(TextChoices):
    CENTRAL_BANK = 'CBI_BANK', _('Central Bank of the Islamic Republic of Iran')  #
    MELLI_BANK = 'BMI', _('Melli bank')  # ملی
    SAMAN_BANK = 'SEP', _('Saman bank')  # سامان
    EGHTESAD_NOVIN_BANK = 'EBANK_BANK', _('Eghtesad novin bank')  # اقتصاد نوین
    PARSIAN_BANK = 'PEC_BANK', _('Parsian bank')  # پارسیان
    PASARGAD_BANK = 'BPI_BANK', _('Pasargad bank')  # بانک پاسارگاد
    POST_BANK = 'POST_BANK', _('Post bank')  # پست بانک ایران
    TEJARAT_BANK = 'TEJARAT_BANK', _('Tejarat bank')  # بانک تجارت
    TOSE_SADERAT_BANK = 'EDBI_BANK', _('Tose saderat bank')  # بانک توسعه صادرات
    REFAH_BANK = 'REFAH_BANK', _('Refah bank')  # بانک توسعه صادرات
    SEPAH_BANK = 'SEPAH_BANK', _('Sepah bank')  # بانک سپه
    SARMAYE_BANK = 'SARMAYE_BANK', _('Sarmaye bank')  # بانک سرمایه
    SADERAT_BANK = 'BSI_BANK', _('Saderat iran bank')  # بانک صادرات ایران
    SANAT_MADAN_BANK = 'BIM_BANK', _('Sanat o madan bank')  # بانک صنعت و معدن
    KARAFARIN_BANK = 'KARAFARIN_BANK', _('Kar afarin bank')  # بانک کارآفرین
    KESHAVARZI_BANK = 'BKI_BANK', _('Keshavarzi bank')  # بانک کشاورزی
    MASKAN_BANK = 'MASKAN_BANK', _('Maskan bank')  # بانک مسکن
    MELLAT_BANK = 'MELLAT_BANK', _('Mellat bank')  # بانک ملت
    TOSE_CREDIT_INSTITUTE = 'CID', _('Credit Institute of Development')  # موسسه اعتباری توسعه

    @classmethod
    def _get_id_dictionary(cls):
        d = {
            cls.CENTRAL_BANK: '010',
            cls.MELLI_BANK: '017',
            cls.SAMAN_BANK: '056',
            cls.EGHTESAD_NOVIN_BANK: '055',
            cls.PARSIAN_BANK: '054',
            cls.PASARGAD_BANK: '057',
            cls.POST_BANK: '021',
            cls.TEJARAT_BANK: '018',
            cls.TOSE_SADERAT_BANK: '020',
            cls.REFAH_BANK: '013',
            cls.SEPAH_BANK: '015',
            cls.SARMAYE_BANK: '058',
            cls.SADERAT_BANK: '019',
            cls.SANAT_MADAN_BANK: '011',
            cls.KARAFARIN_BANK: '053',
            cls.KESHAVARZI_BANK: '016',
            cls.MASKAN_BANK: '014',
            cls.MELLAT_BANK: '012',
            cls.TOSE_CREDIT_INSTITUTE: '051',
        }
        return d

    @DynamicClassAttribute
    def id(self):
        """The id of the Enum member."""
        d = self._get_id_dictionary()
        return d[self.value]

    @classmethod
    def find_by_id(cls, value):
        d = cls._get_id_dictionary()
        for key in d:
            if d[key] == value:
                return key
        raise BankDoesNotExistException()
