<!--![GitHub All Releases](https://img.shields.io/github/downloads/ali-zahedi/az-iranian-bank-intro/total)-->
<!--![GitHub issues](https://img.shields.io/github/issues/ali-zahedi/az-iranian-bank-intro)-->
![GitHub](https://img.shields.io/github/license/ali-zahedi/az-iranian-bank-intro)
![GitHub](https://img.shields.io/pypi/pyversions/az-iranian-bank-intro.svg?maxAge=2592000)
![GitHub](https://img.shields.io/pypi/v/az-iranian-bank-intro.svg?maxAge=2592000)

# AZ Iranian Bank intro

<p dir="rtl">
 کدهای آزاد و متن باز به زبان پایتون (python) که برای استفاده از اطلاعات، اعتبار سنجی درگاه های بانکهای ایرانی توسعه داده شده است.
</p>

🌟 If you ❤️ library, please star it! 🌟

[[_TOC_]]


<h1 dir="rtl">نصب</h1>

<p dir="rtl"> نصب از طریق پکیج منیجر </p>

```pip install az-iranian-bank-intro```


<h1 dir="rtl">نحوه استفاده</h1>

<h2 dir="rtl">اعتبار سنجی کارت ها</h2>

<p dir="rtl">
برای اعتبار سنجی کارت های بانکی کافی است متد اعتبار سنجی را ایمپورت کنیم و شماره کارت مورد نظر را به آن پاس دهیم. در صورتی که شماره کارت مورد نظر معتبر باشد برنامه به کار خود ادامه خواهد داد و در صورتی که نا معتبر باشد exception ارسال خواهد شد. 
</p>

```python
import logging
from azbankintro import card_validate, CardValidationException

try:
    card_validate('6280992042433333')
    logging.debug('کارت معتبر است.')     
except CardValidationException:
    logging.debug('کارت نا معتبر است.')
```


<h2 dir="rtl">اعتبار سنجی IBAN یا شماره شبا</h2>

<p dir="rtl">
برای اعتبار سنجی شماره IBAN کافی است متد اعتبار سنجی را ایمپورت کنیم و شماره IBAN مورد نظر را به آن پاس دهیم. در صورتی که شماره مورد نظر معتبر باشد برنامه به کار خود ادامه خواهد داد و در صورتی که نا معتبر باشد exception ارسال خواهد شد. 
</p>

```python
import logging
from azbankintro import iban_validate, IBANValidationException

try:
    iban_validate('IR062960000000100324200001')
    logging.debug('شماره IBAN معتبر است.')     
except IBANValidationException:
    logging.debug('شماره IBAN نا معتبر است.')
```


<h2 dir="rtl">استفاده از کلاس IBAN</h2>


<h3 dir="rtl">تبدیل شماره حساب به شبا یا IBAN</h2>

<p dir="rtl">
در صورتی که تمایل دارید شماره حساب بانک مورد را تبدیل به شماره شبا کنید می توانید از ساختار زیر استفاده کنید. 
</p>

```python
from azbankintro import *
IBAN.calculate_iban(BankEnum.MELLI_BANK, '0338404829005')
```

<p dir="rtl">
در صورتی که نوع بانک مد نظر را ندارید و فقط رشته آن را دارید می توانید از کد زیر جهت دریافت بانک استفاده کنید. 
</p>

```python
from azbankintro import *
s = 'BMI'
bank_type = BankEnum(s)
IBAN.calculate_iban(bank_type, '0338404829005')
```

<p dir="rtl">
در صورتی که یک instance از نوع IBAN دارید نیز می توانید عملیات اعتبار سنجی را به گونه زیر انجام دهید. 
</p>

```python
from azbankintro import *
s = 'BMI'
bank_type = BankEnum(s)
iban = IBAN.calculate_iban(bank_type, '0338404829005')
iban.validate()
```

<p dir="rtl">
می توانید از فرمتر نیز استفاده کنید. 
</p>

```python
from azbankintro import *
iban = IBAN.calculate_iban(BankEnum.MELLI_BANK, '0338404829005')
print(iban.__str__())
print(iban.format('-'))
print(iban.format(' '))
"""
IR040170000000338404829005
IR04-0170-0000-0033-8404-8290-05
IR04 0170 0000 0033 8404 8290 05
"""
```

# TODO

- [ ] Documentation

- [X] Bank list

- [ ] Logo

- [X] Validate card 

- [X] Validate IBAN

- [X] Calculate IBAN


## توسعه

<p dir="rtl">
 اگر از این بسته استفاده می کنید و خوشتون اومده با دادن ستاره به ما دلگرمی بدید.البته که اگر زمان بگذارید و گسترش بدید خیلی استقبال می کنیم و خوشحال میشیم. البته که در هیچ کدوم از این موارد اصراری نیست. 
</p>
<p dir="rtl">
 شاد باشید و خندون
</p>

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
