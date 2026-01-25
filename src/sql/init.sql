CREATE TABLE receipt_items (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    product_name TEXT NOT NULL,
    --category_id INT REFERENCES categories(id),
    category TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    quantity INTEGER NOT NULL,
    store_address TEXT NOT NULL
);

    /*
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE category_keywords (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id),
    keyword TEXT NOT NULL
);

INSERT
*/