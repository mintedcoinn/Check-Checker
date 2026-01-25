import time
import random
from datetime import datetime
import psycopg2

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

def get_connection():
    while True:
        try:
            conn = psycopg2.connect(psycopg2.connect(
    host="analytics_db",
    port=5432,
    dbname="analytics",
    user="analytics_user",
    password="analytics_pass"
        )
    )
            print("Connected to database")
            return conn
        except psycopg2.OperationalError as e:
            print("Database not ready, retrying in 5 seconds...")
            time.sleep(5)


def main():

    conn = get_connection()
    cursor = conn.cursor()

    while True:
        data = generate_item()

        try:
            cursor.execute(
                """
                INSERT INTO receipt_items
                (timestamp, product_name, category, price, quantity, store_address)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                data
            )
            conn.commit()

        except Exception as e:
            print("Insert failed:", e)
            conn.rollback()
        time.sleep(1)


if __name__ == "__main__":
    main()
