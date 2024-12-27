# from typing import Union
from typing import Union


def get_mask_card_number(number_card_str: Union[str]) -> str:
    """Маскирует номер карты, оставляя видимыми только первые 6 и последние 4 цифры."""
    if len(number_card_str) == 16:
        number_card = ""
        number_count = 0
        for i in number_card_str:
            number_card += i
            number_count += 1
            if number_count == 4:
                number_card += " "
                number_count = 0
        number_card_mask = number_card[:7] + "** ****" + number_card[-6:-1]
        return number_card_mask
    elif len(number_card_str) != 16:
        return "не соответствует длине (16 цифр)"


def get_mask_account(b: Union[str]) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры."""
    if len(b) == 20:
        account_number_mask = "**" + b[-4:]
        return account_number_mask
    elif len(b) != 20:
        return "не соответствует длине (20 цифр)"
