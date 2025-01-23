import json

from src.external_api import loader_apilayer
from src.generators import card_number_generator, filter_by_currency, transact
from src.processing import filter_by_state, sort_by_date
from src.utils import transactions_from_json
from src.widget import get_date, mask_account_card

log_file_masks = "logs/masks.log"
log_file_utils = "logs/utils.log"
with open(log_file_masks, "w"):
    pass
with open(log_file_utils, "w"):
    pass


number_card_or_account = input("Сюда карту|счет: ")
print(mask_account_card(number_card_or_account))

random_date = input("Сюда дату: ")
print(get_date(random_date))

card_list_input = input("Сюда список словарей: ")
card_state_input = input("Сюда опциональный ключ: ")
try:
    print(filter_by_state(eval(card_list_input), card_state_input))
except SyntaxError:
    print("ошибка")

date_list = input("Сюда список словарей даты: ")
reverse = input("Сюда направление True(убывание), False(возрастание) ")
try:
    print(sort_by_date(eval(date_list), reverse))
except SyntaxError:
    print("ошибка")

currency_code_input = input("Введите код валюты: ")
filtered_transactions = filter_by_currency(transact, currency_code_input)

try:
    print(next(filtered_transactions))
except StopIteration:
    print("Конец")

try:
    start_input = int(input("Нижний регистр диапазона"))
    stop_input = int(input("Верхний регистр диапазона"))
    for card_number in card_number_generator(start_input, stop_input):
        print(card_number)
except ValueError:
    print("Ошибка")

print(transactions_from_json("E:/Desktop/Python_Prj/PythonProject1/data/operations.json"))

with open("E:/Desktop/Python_Prj/PythonProject1/data/operations.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    amount_input = data[1]["operationAmount"]["amount"]
    valet_input = data[1]["operationAmount"]["currency"]["code"]

    print(loader_apilayer(amount_input, valet_input))
