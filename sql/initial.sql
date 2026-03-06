CREATE TABLE IF NOT EXISTS receipt_items (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    quantity INTEGER NOT NULL,
    store_address TEXT NOT NULL
);
