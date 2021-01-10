from azbankintro.exceptions import IBANValidationException

def iban_validate(value):
    character_mapping = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
    }

    if len(value) != 26:
        raise IBANValidationException()

    new_value = value[4:]
    for item in value[:2]:
        new_value = new_value + str(character_mapping[item])
    new_value = new_value + value[2:4]

    if len(value) != 28:
        raise IBANValidationException()

    if int(new_value) % 97 != 1:
        raise IBANValidationException
