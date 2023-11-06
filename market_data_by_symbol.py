import requests
import pandas as pd


def fetch_monthly_adjusted(symbol):
    # Define the API endpoint and parameters
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_MONTHLY_ADJUSTED",
        "symbol": symbol,
        "apikey": "USAYSNCYKM7VRBXG"
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check for a valid response
    if response.status_code == 200:

        # Parse the JSON response
        data = response.json()

        # 'data's' type equals to dictionary containing the API response
        monthly_data = data['Monthly Adjusted Time Series']

        # Convert the dictionary to a DataFrame
        df = pd.DataFrame.from_dict(monthly_data, orient='index')

        # Convert the index to datetime for better handling
        df.index = pd.to_datetime(df.index)
        print(df.dtypes)
        print(df.info())

        # column names to be more descriptive
        df.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted Close', 'Volume', 'Dividend Amount']

        # Convert the attributes' types to numeric values
        df['Open'] = pd.to_numeric(df['Open'])
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df['Close'] = pd.to_numeric(df['Close'])
        df['Adjusted Close'] = pd.to_numeric(df['Adjusted Close'])
        df['Volume'] = pd.to_numeric(df['Volume'])
        df['Dividend Amount'] = pd.to_numeric(df['Dividend Amount'])
        df['change'] = ((df['Close'] - df['Open'])/df['Close'])*100.0
        print(df.dtypes)

        return df

    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

