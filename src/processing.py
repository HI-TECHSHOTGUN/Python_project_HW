def filter_by_state(not_filtered_list: list[dict], state: str) -> list:
    """Функция для сортировки по состоянию операций"""
    if state != "CANCELED":
        state = "EXECUTED"
    filtered_state_list = []
    for item in not_filtered_list:
        if item.get("state") == state:
            filtered_state_list.append(item)

    return filtered_state_list


def sort_by_date(data: list[dict], reverse: str) -> list[dict] or str:
    """Функция для сортировки даты по убыванию"""
    count_error = 0
    count_cikle = 0
    for k in data:
        date_true = k["date"]
        if (
            date_true[4] == "-"
            and date_true[7] == "-"
            and date_true[13] == ":"
            and date_true[16] == ":"
            and date_true[19] == "."
        ):
            count_error += 1
        count_cikle += 1
    if count_error == count_cikle:
        if reverse == "False":
            sorted_data = sorted(data, key=lambda item: tuple(map(int, item["date"][:10].split("-"))), reverse=False)
            return sorted_data
        elif reverse == "True" or reverse != "True":
            sorted_data = sorted(data, key=lambda item: tuple(map(int, item["date"][:10].split("-"))), reverse=True)
            return sorted_data
    else:
        return "Ошибка в вводе данных"
