def iban_parser(value):
    cc = value[:2]
    cd = value[2:4]
    bank_id = value[4:7]
    account_type = value[7]
    account_number = value[8:]
    return cc, cd, bank_id, account_type, account_number

def iban_to_number(value):
    cc, cd, bank_id, account_type, account_number = iban_parser(value)
    new_value = f'{bank_id}{account_type}{account_number}'
    for item in cc:
        new_value = new_value + str(_character_map()[item])
    new_value = new_value + cd
    return new_value


def _character_map():
    character_mapping = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
    }
    return character_mapping
