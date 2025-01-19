import json
import os


def transactions_from_json(file):
    if not isinstance(file, str):
        print("Ошибка: Путь к файлу должен быть строкой")
        return []

    if not os.path.exists(file):
        print(f"Ошибка: файл {file} не найден")
        return []

    if os.stat(file).st_size == 0:
        print(f"Ошибка: файл {file} пустой.")
        return []
    try:
        with open(file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)

            except json.JSONDecodeError:
                print("Ошибка: Некорректный JSON")
                return []

        if isinstance(data, list):
            return data

        else:
            print("Ошибка: JSON файл должен содержать список")
            return []

    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return []
