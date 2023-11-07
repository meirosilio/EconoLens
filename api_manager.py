# api_manager.py
import requests
import pandas as pd

class APIManager:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def fetch_data(self, function, symbol):
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            # Parse data and create DataFrame here if needed
            return data
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return None
