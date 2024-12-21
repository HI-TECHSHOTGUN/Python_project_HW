import pytest

from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def test_get_mask_card_number_error(test_numbers_card_error):
    assert get_mask_card_number(test_numbers_card_error) == "не соответствует длине (16 цифр)"

    # 73654108430135874305


def test_get_mask_card_number(test_numbers_card):
    assert get_mask_card_number(test_numbers_card) == "4879 32** **** 0115"


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

    assert mask_account_card("Счет 7365410843013587") == "Счет не соответствует длине (20 цифр)"

    assert mask_account_card("Visa Platinum 70007922896") == "Visa Platinum не соответствует длине (16 цифр)"


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
