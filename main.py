from src.widget import get_date, mask_account_card

number_card_or_account = input("Сюда карту|счет: ")
print(mask_account_card(number_card_or_account))
random_date = input("Сюда дату: ")
print(get_date(random_date))
