from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date


number_card_or_account = input("Сюда карту|счет: ")
print(mask_account_card(number_card_or_account))
random_date = input("Сюда дату: ")
print(get_date(random_date))
card_list_input = input("Сюда список словарей: ")
card_state_input = input("юда опциональный ключ: ")
print(filter_by_state(eval(card_list_input), card_state_input))
date_list = input("Сюда список словарей даты: ")
print(sort_by_date(eval(date_list)))
