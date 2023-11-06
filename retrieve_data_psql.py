import psycopg2
import pandas as pd

def retrieve_monthly_data(symbol, columns):
    try:
        # Define database parameters
        db_params = {
            "database": "econo_lens_db",
            "user": "postgres",
            "password": "5343153",
            "host": "localhost",
            "port": "5432"
        }

        # Establish a connection to the database
        conn = psycopg2.connect(**db_params)

        # Construct the SQL query dynamically based on the symbol and columns
        select_query = f"""
            SELECT date, {', '.join(columns)}
            FROM market_data
            WHERE symbol_id = (SELECT symbol_id FROM symbols WHERE symbol = %s)
            ORDER BY date;
        """

        # Use pandas to read data directly into a DataFrame with a parameterized query
        df = pd.read_sql_query(select_query, conn, params=(symbol,))

        # Close the connection
        conn.close()

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None

