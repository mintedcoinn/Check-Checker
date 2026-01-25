import time
import random
from datetime import datetime
import psycopg2
import config

PRODUCTS = [
    ("Молоко 2.5%", "Молочные продукты", 89.90),
    ("Хлеб пшеничный", "Продукты", 45.00),
    ("Яблоки", "Фрукты", 120.00),
    ("Куриное филе", "Мясо", 320.00),
    ("Шоколад", "Сладости", 95.50),
    ("Кофе молотый", "Напитки", 399.00)
]

ADDRESSES = [
    "г. Владивосток, ул. Светланская, 15",
    "г. Владивосток, пр. Океанский, 88",
    "г. Владивосток, ул. Русская, 42"
]

def generate_item():
    product_name, category, price = random.choice(PRODUCTS)
    quantity = random.randint(1, 5)
    store_address = random.choice(ADDRESSES)

    return (
        datetime.now(),
        product_name,
        category,
        price,
        quantity,
        store_address
    )

def main():

    conn = psycopg2.connect(**config.DB_CONFIG)
    cursor = conn.cursor()

    while True:
        data = generate_item()

        cursor.execute(
            """
            INSERT INTO receipt_items
            (timestamp, product_name, category, price, quantity, store_address)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            data
        )

        conn.commit()
        time.sleep(1)

if __name__ == "__main__":
    main()
