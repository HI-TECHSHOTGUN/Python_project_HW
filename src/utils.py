import json
import logging
import os

MASTER_DIR = os.path.dirname(os.path.dirname(__file__))

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(MASTER_DIR, 'logs', "utils.log"), encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_from_json(file) -> list:
    """Считывает данные из .json файла"""
    logger.info("Проверка входящих данных по типу")
    if not isinstance(file, str):
        logger.error("Ошибка: Путь к файлу должен быть строкой")
        return []

    logger.info("Поиск файла в проекте")
    if not os.path.exists(file):
        logger.error(f"Ошибка: файл {file} не найден")
        return []

    logger.info("Проверка файла на содержание данных")
    if os.stat(file).st_size == 0:
        logger.error(f"Ошибка: файл {file} пустой.")
        return []
    try:
        with open(file, "r", encoding="utf-8") as f:
            logger.info("Запись данных в переменную")
            try:
                data = json.load(f)
                logger.info("Успех, запись произведена")

            except json.JSONDecodeError:
                logger.error("Ошибка")
                return []

        logger.info("Проверка переменной на соотношения по типу")
        if isinstance(data, list):
            logger.info("Успех, возврат данных")
            return data

        else:
            logger.error("Ошибка проверки")
            return []

    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")
        return []
