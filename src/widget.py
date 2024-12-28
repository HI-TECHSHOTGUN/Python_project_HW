from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: Union[str]) -> str:
    """маскировка номера карты с выводом названия карты или счета"""
    final_result = ""
    if number.lower().startswith("счет"):
        """маскировка счета"""
        name_account = ""
        count_number = 0
        for i in number:
            if i.isalpha() or i == " ":
                name_account += i
                count_number += 1

        final_result = name_account.title() + get_mask_account(number[count_number:])
    elif number[0:4].lower() != "счет":
        """маскировка карты"""
        number_card = ""
        count_word = 0
        for i in number:
            if i.isalpha() or i == " ":
                number_card += i
                count_word += 1

        final_result = number_card + get_mask_card_number(number[count_word:])
    return final_result


def get_date(date: str) -> str:
    """Извлекает дату из строки в формате "YYYY-MM-DDTHH:MM:SS.ffffff" и форматирует её как "DD.MM.YYYY" """
    if date == "":
        return 'Неверный формат даты. (Пример: "YYYY-MM-DDTHH:MM:SS.ffffff")'
    elif (
        date[0] == '"'
        and date[5] == "-"
        and date[8] == "-"
        and date[14] == ":"
        and date[17] == ":"
        and date[20] == "."
        and date[-1] == '"'
    ):
        return f'"{date[9:11]}.{date[6:8]}.{date[1:5]}"'
    else:
        return 'Неверный формат даты. (Пример: "YYYY-MM-DDTHH:MM:SS.ffffff")'
