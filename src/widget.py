from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: Union[str]) -> str:
    final_result = ""
    if number[0:4].lower() == "счет":
        name_account = ""
        count_number = 0
        for i in number:
            if i.isalpha() or i == " ":
                name_account += i
                count_number += 1

        final_result = name_account + get_mask_account(number[count_number:])
    elif number[0:4].lower() != "счет":
        number_card = ""
        count_word = 0
        for i in number:
            if i.isalpha() or i == " ":
                number_card += i
                count_word += 1

        final_result = number_card + get_mask_card_number(number[count_word:])
    return final_result


def get_date(date: Union[str]) -> str:
    date_list = date[1:11].split("-")
    date_list.reverse()
    date_str = ".".join(date_list)
    return f'"{date_str}"'
