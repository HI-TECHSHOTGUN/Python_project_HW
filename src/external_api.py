import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def loader_apilayer(amount: float, valet: str):
    """Функция для конвертации валют"""
    try:
        if valet != "RUB" and valet != "USD" and valet != "EUR":
            valet = "RUB"
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={valet}&amount={amount}"
        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()
        # status_code = response.status_code
        # print(status_code)
        return f'{amount} в {valet} равен {result["result"]} в RUB'
    except json.JSONDecodeError as e:
        print(f"Ошибка ввода данных {e}")
