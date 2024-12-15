from typing import Union


def filter_by_state(data: Union[list], state='EXECUTED') ->list:
    filtered_1 = []
    for item in data:
        if item.get('state') == state:
            filtered_1.append(item)

    return filtered_1


