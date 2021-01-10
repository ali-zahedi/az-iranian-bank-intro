from azbankintro.exceptions import CardValidationException


def card_validate(value):
    if not len(value) == 16:
        raise CardValidationException()

    items = []
    for i in range(0, len(value)):
        k = ((i + 1) % 2) + 1
        r = k * int(value[i])
        items.append(r - 9 if r >= 10 else r)

    if sum(items) % 10 != 0:
        raise CardValidationException()
