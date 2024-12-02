from src.masks import get_mask_account, get_mask_card_number

number_card = input()
print(get_mask_card_number(number_card))
number_account = input()
print(get_mask_account(number_account))
