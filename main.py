# import json
import os

# from src.external_api import loader_apilayer
# from src.generators import card_number_generator, filter_by_currency, transact
from src.module_pd import read_csv, read_xlsx
from src.processing import filter_by_state, sort_by_date
from src.sort_re_funcs import search_by_string
from src.utils import transactions_from_json
from src.widget import get_date, mask_account_card

MASTER_DIR = os.path.dirname(os.path.abspath(__file__))
DIR_JSON = os.path.join(MASTER_DIR, "data", "operations.json")
"""Нужно для построения пути до файла"""

log_file_masks = "logs/masks.log"
log_file_utils = "logs/utils.log"
with open(log_file_masks, "w"):
    pass
with open(log_file_utils, "w"):
    pass


# number_card_or_account = input("Сюда карту|счет: ")
# print(mask_account_card(number_card_or_account))
#
# random_date = input("Сюда дату: ")
# print(get_date(random_date))
#
# card_list_input = input("Сюда список словарей: ")
# card_state_input = input("Сюда опциональный ключ: ")
# try:
#     print(filter_by_state(eval(card_list_input), card_state_input))
# except SyntaxError:
#     print("ошибка")
#
# date_list = input("Сюда список словарей даты: ")
# reverse = input("Сюда направление True(убывание), False(возрастание) ")
# try:
#     print(sort_by_date(eval(date_list), reverse))
# except SyntaxError:
#     print("ошибка")
#
# currency_code_input = input("Введите код валюты: ")
# filtered_transactions = filter_by_currency(transact, currency_code_input)
#
# try:
#     print(next(filtered_transactions))
# except StopIteration:
#     print("Конец")
#
# try:
#     start_input = int(input("Нижний регистр диапазона"))
#     stop_input = int(input("Верхний регистр диапазона"))
#     for card_number in card_number_generator(start_input, stop_input):
#         print(card_number)
# except ValueError:
#     print("Ошибка")
#
# print(transactions_from_json(os.path.join(MASTER_DIR, "data", "operations.json")))
#
# with open(DIR_JSON, "r", encoding="utf-8") as f:
#     data = json.load(f)
#     amount_input = data[1]["operationAmount"]["amount"]
#     valet_input = data[1]["operationAmount"]["currency"]["code"]
#
#     print(loader_apilayer(amount_input, valet_input))
#
# path_excel = input("Введите имя считываемого файла excel: ")
# print(read_xlsx(os.path.join(MASTER_DIR, "data", path_excel)))
# # transactions_excel.xlsx
#
# path_csv = input("Введите имя считываемого файла cvs: ")
# print(read_csv(os.path.join(MASTER_DIR, "data", path_csv)))
# # transactions.csv


def main():
    """Общая функция по сборке всего проекта"""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла
            """
        )
        answer_1 = input("Введите число: ")

        if answer_1 == "1":
            print("Для обработки выбран JSON-файл")
            operations = transactions_from_json(os.path.join(MASTER_DIR, "data", "operations.json"))
            break
        elif answer_1 == "2":
            print("Для обработки выбран CSV-файл")
            operations = read_csv(os.path.join(MASTER_DIR, "data", "transactions.csv"))
            break
        elif answer_1 == "3":
            print("Для обработки выбран Excel-файл")
            operations = read_xlsx(os.path.join(MASTER_DIR, "data", "transactions_excel.xlsx"))
            break
        else:
            print("\nОшибка ввода! Такого пункта не существует.\nПопробуйте ещё раз.\n ")

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        answer_2 = input("Ваш ответ: ").upper()

        if answer_2 == "EXECUTED" or answer_2 == "CANCELED" or answer_2 == "PENDING":
            filtered_operations = filter_by_state(operations, answer_2)
            print(f"Операции отфильтрованы по статусу {answer_2}")
            break
        else:
            print(f"Статус операции {answer_2} недоступен.\nПопробуйте снова.\n ")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        filter1 = input("Введите 'да' или 'нет': ").lower()

        if filter1 == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            filter1_1 = input("по возрастанию/по убыванию: ").lower()
            if filter1_1 == "по убыванию":
                filtered_operations_dy_date = sort_by_date(filtered_operations, "True")
                break
            elif filter1_1 == "по возрастанию":
                filtered_operations_dy_date = sort_by_date(filtered_operations, "False")
                break
            else:
                print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")
        elif filter1 == "нет":
            filtered_operations_dy_date = filtered_operations
            break
        else:
            print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        filter2 = input("Введите 'да' или 'нет': ").lower()

        if filter2 == "да":
            filtered_operations_dy_currency = []
            for operation in filtered_operations_dy_date:
                if answer_1 == "1":
                    if operation["operationAmount"]["currency"]["code"] == "RUB":
                        filtered_operations_dy_currency.append(operation)
                elif answer_1 == "2" or answer_1 == "3":
                    if operation["currency_code"] == "RUB":
                        filtered_operations_dy_currency.append(operation)
            if len(filtered_operations_dy_currency) == 0:
                return "Рублевые транзакции не найдены"
            else:
                break
        elif filter2 == "нет":
            filtered_operations_dy_currency = filtered_operations_dy_date
            break
        else:
            print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter3 = input("Введите 'да' или 'нет': ").lower()

        if filter3 == "да":
            user_search = input("Введите слово или фразу для поиска: ")
            filtered_operations_dy_descr = search_by_string(filtered_operations_dy_currency, user_search)
            break
        elif filter3 == "нет":
            filtered_operations_dy_descr = filtered_operations_dy_currency
            break
        else:
            print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")

    if len(filtered_operations_dy_descr) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return []

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_operations_dy_descr)}\n ")

    for operation in filtered_operations_dy_descr:
        date = get_date(operation.get("date"))
        description = operation.get("description")
        print(f"{date} {description}")

        if operation.get("description") == "Открытие вклада":
            acc_number = mask_account_card(operation["to"])
            print(acc_number)
            if answer_1 == "1":
                amount = operation["operationAmount"]["amount"]
                currency_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {amount} {currency_name}")
            elif answer_1 == "2" or answer_1 == "3":
                amount = operation["amount"]
                currency_name = operation["currency_name"]
                print(f"Сумма: {amount} {currency_name}")
        else:
            acc_number_from = mask_account_card(operation["from"])
            acc_number_to = mask_account_card(operation["to"])
            print(f"{acc_number_from} -> {acc_number_to}")
            if answer_1 == "1":
                amount = operation["operationAmount"]["amount"]
                currency_name = operation["operationAmount"]["currency"]["name"]
                print(f"Сумма: {amount} {currency_name}")
            elif answer_1 == "2" or answer_1 == "3":
                amount = operation["amount"]
                currency_name = operation["currency_name"]
                print(f"Сумма: {amount} {currency_name}")
        print()


if __name__ == "__main__":
    result = main()
