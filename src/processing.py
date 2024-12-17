

def filter_by_state(not_filtered_list: list[dict], state: str) -> list:
    """Функция для сортировки по состоянию операций"""
    if state != "CANCELED":
        state = "EXECUTED"
    filtered_state_list = []
    for item in not_filtered_list:
        if item.get("state") == state:
            filtered_state_list.append(item)

    return filtered_state_list


def sort_by_date(data: list[dict], reverse: bool = True) -> list:
    """Функция для сортировки даты по убыванию"""
    sorted_data = sorted(data, key=lambda item: tuple(map(int, item["date"][:10].split("-"))), reverse=reverse)

    return sorted_data
