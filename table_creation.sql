
CREATE TABLE symbols (
    symbol_id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    company_name VARCHAR(255)
);

CREATE TABLE market_data (
    data_id SERIAL PRIMARY KEY,
    symbol_id INT REFERENCES symbols(symbol_id),
    date DATE NOT NULL,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    adjusted_close NUMERIC,
    volume BIGINT,
    dividend_amount NUMERIC
);

ALTER TABLE market_data
ADD COLUMN change FLOAT;

UPDATE market_data
SET change = ((close - open)/close)*100;



