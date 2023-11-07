from sqlalchemy import create_engine
from connection_manager import get_db_config

def insert_market_data(symbol, df):
    try:
        # Get database connection parameters from config
        db_params = get_db_config()

        # Create a database connection
        connection_string = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
        engine = create_engine(connection_string)
        conn = engine.raw_connection()
        cursor = conn.cursor()

        # Check if the symbol already exists in the 'symbols' table
        cursor.execute("SELECT symbol_id FROM symbols WHERE symbol = %s;", (symbol,))
        symbol_result = cursor.fetchone()

        # If the symbol doesn't exist, insert it into the 'symbols' table
        if symbol_result is None:
            cursor.execute("INSERT INTO symbols (symbol) VALUES (%s) RETURNING symbol_id;", (symbol,))
            symbol_id = cursor.fetchone()[0]
        else:
            symbol_id = symbol_result[0]

        # Loop through the DataFrame and insert rows into the 'market_data' table
        for index, row in df.iterrows():
            date = index.date()
            open_price = row['Open']
            high_price = row['High']
            low_price = row['Low']
            close_price = row['Close']
            adjusted_close = row['Adjusted Close']
            volume = row['Volume']
            dividend_amount = row['Dividend Amount']
            change = row['change']

            cursor.execute("""
                INSERT INTO market_data (symbol_id, date, open, high, low, close, adjusted_close, volume, dividend_amount, change)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (symbol_id, date, open_price, high_price, low_price, close_price, adjusted_close, volume, dividend_amount, change))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Data successfully inserted into the database.")
    except Exception as e:
        print(f"Error: {e}")


