import pytest


@pytest.fixture
def test_numbers_card_error():
    return '51726345'

@pytest.fixture
def test_numbers_card():
    return '4879328423140115'

@pytest.fixture
def test_get_data_fix():
    return '"11.03.2024"'

@pytest.fixture
def test_get_data_message():
    return 'Неверный формат даты. (Пример: "YYYY-MM-DDTHH:MM:SS.ffffff")'

@pytest.fixture
def test_filter_by_state_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def test_sort_by_date_false():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

@pytest.fixture
def test_sort_by_date_true():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def test_sort_by_date_clone():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

@pytest.fixture
def test_sort_by_date_none_tipical():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '201:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:2964'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-0T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35364'}]

