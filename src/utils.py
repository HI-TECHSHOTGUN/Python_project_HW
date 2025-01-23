import json
import os
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_from_json(file)-> list:
    """Считывает данные из .json файла"""
    logger.info(f'Проверка входящих данных по типу')
    if not isinstance(file, str):
        logger.error("Ошибка: Путь к файлу должен быть строкой")
        return []

    logger.info(f'Поиск файла в проекте')
    if not os.path.exists(file):
        logger.error(f"Ошибка: файл {file} не найден")
        return []

    logger.info(f'Проверка файла на содержание данных')
    if os.stat(file).st_size == 0:
        logger.error(f"Ошибка: файл {file} пустой.")
        return []
    try:
        with open(file, "r", encoding="utf-8") as f:
            logger.info(f'Запись данных в переменную')
            try:
                data = json.load(f)
                logger.info(f'Успех, запись произведена')

            except json.JSONDecodeError:
                logger.error(f'Ошибка')
                return []

        logger.info(f'Проверка переменной на соотношения по типу')
        if isinstance(data, list):
            logger.info(f'Успех, возврат данных')
            return data

        else:
            logger.error(f'Ошибка проверки')
            return []

    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")
        return []
