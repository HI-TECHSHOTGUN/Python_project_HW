from typing import Union


def get_mask_card_number(a: Union[str]) -> str:
    """Маскирует номер карты, оставляя видимыми только первые 6 и последние 4 цифры."""
    if len(a) == 16 and a.isdigit():
        number_card = ""
        number_count = 0
        for i in a:
            number_card += i
            number_count += 1
            if number_count == 4:
                number_card += " "
                number_count = 0
        number_card_mask = number_card[:7] + "** ****" + number_card[-6:]
        return number_card_mask
    else:
        print("Не корректные данные")
        return ""


def get_mask_account(b: Union[str]) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры."""
    if len(b) == 20 and b.isdigit():
        account_number_mask = "**" + b[-4:]
        return account_number_mask
    else:
        print("Не корректные данные")
        return ""
