import pytest

from src.generators import card_number_generator, filter_by_currency, transact, transaction_descriptions
from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def test_get_mask_card_number_error(test_numbers_card_error):
    assert get_mask_card_number(test_numbers_card_error) == "не соответствует длине (16 цифр)"

    # 73654108430135874305


def test_get_mask_card_number(test_numbers_card):
    assert get_mask_card_number(test_numbers_card) == "4879 32** **** 0115"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 7365410843013587", "Счет не соответствует длине (20 цифр)"),
        ("Visa Platinum 70007922896", "Visa Platinum не соответствует длине (16 цифр)"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

    assert mask_account_card(value) == expected

    assert mask_account_card(value) == expected

    assert mask_account_card(value) == expected


def test_get_date(test_get_data_fix, test_get_data_message):
    assert get_date('"2024-03-11T02:26:18.671407"') == test_get_data_fix

    assert get_date('2024-03-11T02:26:18.671407"') == test_get_data_message

    assert get_date("") == test_get_data_message


def test_filter_by_state(test_filter_by_state_list):
    assert filter_by_state(test_filter_by_state_list, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(test_filter_by_state_list, "NOT_List") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize("test_state", ["LOL", "TESTS_STATE", "NONE_STATE"])
def test_parametrize_filter_by_state(test_filter_by_state_list, test_state):
    assert filter_by_state(test_filter_by_state_list, test_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(
    test_sort_by_date_false,
    test_sort_by_date_true,
    test_filter_by_state_list,
    test_sort_by_date_clone,
    test_sort_by_date_none_tipical,
):
    assert sort_by_date(test_filter_by_state_list, "False") == test_sort_by_date_false
    assert sort_by_date(test_filter_by_state_list, "True") == test_sort_by_date_true

    assert sort_by_date(test_sort_by_date_clone, "True") == test_sort_by_date_clone
    assert sort_by_date(test_sort_by_date_clone, "False") == test_sort_by_date_clone

    assert sort_by_date(test_sort_by_date_none_tipical, "True") == "Ошибка в вводе данных"
    assert sort_by_date(test_sort_by_date_none_tipical, "False") == "Ошибка в вводе данных"


def test_filter_by_currency():
    usd_transactions = list(filter_by_currency(transact, "USD"))
    assert len(usd_transactions) == 3
    for transaction in usd_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_with_data():
    expected_usd_transactions = [
        transact[0],
        transact[1],
        transact[3],
    ]
    usd_transactions = list(filter_by_currency(transact, "USD"))
    assert usd_transactions == expected_usd_transactions

    expected_rub_transactions = [transact[2], transact[4]]
    rub_transactions = list(filter_by_currency(transact, "RUB"))
    assert rub_transactions == expected_rub_transactions


def test_valid_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions) == 4


def test_transaction_descriptions_with_no_transactions():
    empty_transactions_iter = filter_by_currency([], "USD")
    descriptions = list(transaction_descriptions(empty_transactions_iter))
    assert descriptions == []


def test_empty_transactions():
    descriptions = list(transaction_descriptions([]))
    assert len(descriptions) == 0


@pytest.mark.parametrize(
    "num_1, num_2, result",
    [
        (
            10,
            15,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
                "0000 0000 0000 0014",
                "0000 0000 0000 0015",
            ],
        ),
        (
            23456789,
            23456793,
            [
                "0000 0000 2345 6789",
                "0000 0000 2345 6790",
                "0000 0000 2345 6791",
                "0000 0000 2345 6792",
                "0000 0000 2345 6793",
            ],
        ),
        (734865, 734865, ["0000 0000 0073 4865"]),
        (
            6457897645,
            6457897650,
            [
                "0000 0064 5789 7645",
                "0000 0064 5789 7646",
                "0000 0064 5789 7647",
                "0000 0064 5789 7648",
                "0000 0064 5789 7649",
                "0000 0064 5789 7650",
            ],
        ),
    ],
)
def test_valid_range(num_1, num_2, result):
    generated_cards = list(card_number_generator(num_1, num_2))
    assert generated_cards == result


def test_single_card():
    expected_card = ["1234 5678 9012 3456"]
    generated_cards = list(card_number_generator(1234567890123456, 1234567890123456))
    assert generated_cards == expected_card


def test_large_range():
    cards = list(card_number_generator(9999999999999995, 9999999999999999))
    assert len(cards) == 5
    assert cards[0] == "9999 9999 9999 9995"
    assert cards[-1] == "9999 9999 9999 9999"
