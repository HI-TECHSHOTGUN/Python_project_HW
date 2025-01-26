import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card_str: Union[str]) -> str:
    """Маскирует номер карты, оставляя видимыми только первые 6 и последние 4 цифры."""
    try:
        logger.info("Проверка данных на пригодность")
        if len(number_card_str) == 16:
            number_card = ""
            number_count = 0
            logger.info("Начало работы цикла")
            for i in number_card_str:
                number_card += i
                number_count += 1
                if number_count == 4:
                    number_card += " "
                    number_count = 0
            logger.info("Конец работы цикла")
            number_card_mask = number_card[:7] + "** ****" + number_card[-6:-1]
            return number_card_mask
        elif len(number_card_str) != 16:
            logger.error("Ошибка длинны по входным данным")
            return "не соответствует длине (16 цифр)"
    except Exception as e:
        logger.error(f"Непредвиденная ошибка {e}")


def get_mask_account(b: Union[str]) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры."""
    try:
        if len(b) == 20:
            logger.info("Обработка данных")
            account_number_mask = "**" + b[-4:]
            logger.info("Обработка завершена, успех")
            return account_number_mask
        elif len(b) != 20:
            logger.error("Ошибка длинны по входным данным")
            return "не соответствует длине (20 цифр)"

    except Exception as e:
        logger.error(f"Непредвиденная ошибка {e}")
