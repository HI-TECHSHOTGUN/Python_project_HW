from typing import Union


def filter_by_state(x: Union[list], state: str= "EXECUTED") -> list:
    """Функция для сортировки по состоянию операций"""
    filtered_1 = []
    for item in x:
        if item.get("state") == state:
            filtered_1.append(item)

    return filtered_1


def sort_by_date(data: Union[list], reverse: bool = True) -> list:
    """Функция для сортировки даты по убыванию"""
    sorted_data = sorted(data, key=lambda item: tuple(map(int, item["date"][:10].split("-"))), reverse=reverse)

    return sorted_data
