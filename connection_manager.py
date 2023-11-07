import configparser

def get_db_config():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Adjust the path if needed

    db_params = {
        "database": config['database']['dbname'],
        "user": config['database']['user'],
        "password": config['database']['password'],
        "host": config['database']['host'],
        "port": config['database']['port']
    }

    return db_params

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Adjust the path if needed
    return config['api']['alphavantage_api_key']