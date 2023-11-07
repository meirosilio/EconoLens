import market_data_by_symbol
import data_insertion_psql
import retrieve_data_psql



def process_symbol_data(symbol, columns_to_retrieve):

    # Retrieve data from the database
    df = retrieve_data_psql.retrieve_monthly_data(symbol, columns_to_retrieve)
    print(df)

    # Check if the DataFrame is not empty
    if not df.empty:
        print(f"Retrieving data from DB for symbol: {symbol}...")
        print(df.head())
    else:
        print(f"Making API call for symbol: {symbol}...")
        # Make the API call to fetch monthly adjusted data for the symbol
        df_symbol = market_data_by_symbol.fetch_monthly_adjusted(symbol)

        # Insert data into the database
        data_insertion_psql.insert_market_data(symbol, df_symbol)

        # Retrieve the data from the database again
        df = retrieve_data_psql.retrieve_monthly_data(symbol, columns_to_retrieve)
        print(df.head())


if __name__ == "__main__":
    # calling to the function:
    symbol = 'IBM'
    columns_to_retrieve = ['open', 'close', 'change']
    process_symbol_data(symbol, columns_to_retrieve)
