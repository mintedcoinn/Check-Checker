CREATE TABLE receipt_items (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    quantity INTEGER NOT NULL,
    store_address TEXT NOT NULL
);
