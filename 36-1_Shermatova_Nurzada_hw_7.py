
import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

conn.commit()


def add_products():
    products_data = [
        ('Товар 1', 50.99, 10),
        ('Товар 2', 99.5, 20),

    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products_data)
    conn.commit()


def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()


def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()


def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()


def print_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def print_products_below_limit():
    cursor.execute('SELECT * FROM products WHERE price < 100 AND quantity > 5')
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_products_by_title(keyword):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + keyword + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)


add_products()
print_all_products()

update_quantity(1, 15)
update_price(2, 120.0)

print_all_products()

delete_product(3)

print_all_products()

print_products_below_limit()

search_products_by_title('Товар')


