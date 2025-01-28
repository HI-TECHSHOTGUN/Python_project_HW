import pandas as pd


def read_csv(file_name_csv):
    """Функция для чтения файлов с расширением .csv"""
    try:
        csv_dict = pd.read_csv(file_name_csv)
        csv_list = csv_dict.to_dict(orient="records")

        return csv_list

    except Exception as e:
        print(f"Ошибка {e}")
        return []


def read_xlsx(file_name_excel):
    """Функция для чтения файлов с расширением .xlsx"""
    try:
        xlsx_dict = pd.read_excel(file_name_excel)
        xlsx_list = xlsx_dict.to_dict(orient="records")

        return xlsx_list

    except Exception as e:
        print(f"Ошибка {e}")
        return []
