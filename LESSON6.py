

import sqlite3

def create_connection(db_file):
    """Tạo kết nối tới cơ sở dữ liệu SQLite"""
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    """Tạo bảng products"""
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL,
        quantity INTEGER
    )
    ''')
    conn.commit()

def insert_product(conn, product):
    """Chèn một sản phẩm vào bảng products"""
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)
    ''', product)
    conn.commit()

def update_product(conn, name, price, quantity):
    """Cập nhật thông tin sản phẩm trong bảng products"""
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE products
    SET price = ?, quantity = ?
    WHERE name = ?
    ''', (price, quantity, name))
    conn.commit()

def fetch_products(conn):
    """Truy vấn tất cả các sản phẩm từ bảng products"""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    return products

def main():
    database = "products.db"

    # Tạo kết nối tới cơ sở dữ liệu
    conn = create_connection(database)

    # Tạo bảng products
    create_table(conn)

    # Chèn một số sản phẩm mẫu vào bảng products
    insert_product(conn, ('Apple', 0.5, 100))
    insert_product(conn, ('Banana', 0.3, 150))
    insert_product(conn, ('Orange', 0.7, 200))

    # Cập nhật dữ liệu trong bảng products
    update_product(conn, 'Apple', 10, 200)

    # Truy vấn và hiển thị các sản phẩm
    products = fetch_products(conn)
    print("Products:")
    for product in products:
        print(product)

    # Đóng kết nối
    conn.close()

if __name__ == '__main__':
    main()