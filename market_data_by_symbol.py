import pandas as pd
from api_manager import APIManager
from connection_manager import get_api_key

# Create an instance of APIManager for the Alphavantage API
alphavantage_api = APIManager(base_url="https://www.alphavantage.co/query", api_key=get_api_key())


def fetch_monthly_adjusted(symbol):
    try:
        # Make the API call using the APIManager instance
        data = alphavantage_api.fetch_data(function="TIME_SERIES_MONTHLY_ADJUSTED", symbol=symbol)

        if data:
            # Parse the data and create a DataFrame
            monthly_data = data.get('Monthly Adjusted Time Series', {})
            df = pd.DataFrame.from_dict(monthly_data, orient='index')

            # Convert the index to datetime for better handling
            df.index = pd.to_datetime(df.index)
            print(df.dtypes)
            print(df.info())

            # Column names for better description
            df.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted Close', 'Volume', 'Dividend Amount']

            # Convert attribute types to numeric values
            df['Open'] = pd.to_numeric(df['Open'])
            df['High'] = pd.to_numeric(df['High'])
            df['Low'] = pd.to_numeric(df['Low'])
            df['Close'] = pd.to_numeric(df['Close'])
            df['Adjusted Close'] = pd.to_numeric(df['Adjusted Close'])
            df['Volume'] = pd.to_numeric(df['Volume'])
            df['Dividend Amount'] = pd.to_numeric(df['Dividend Amount'])
            df['change'] = ((df['Close'] - df['Open']) / df['Close']) * 100.0
            print(df.dtypes)

            return df
        else:
            print("Failed to retrieve data.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
