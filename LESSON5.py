import sqlite3

# Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
conn = sqlite3.connect("lesson5.db")

# Tạo đối tượng để điều khiển cơ sở dữ liệu
cursor = conn.cursor()

# Tạo bảng tasks với bốn trường thông tin
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    due_date TEXT
)
''')

# Tạo bảng users với bốn trường thông tin
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TEXT
)
''')

# Lưu các thay đổi
conn.commit()

# Truy vấn dữ liệu từ bảng tasks
cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()

# Hiển thị dữ liệu từ bảng tasks
print("Tasks:")
for task in tasks:
    print(task)

# Truy vấn dữ liệu từ bảng users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

# Hiển thị dữ liệu từ bảng users
print("\nUsers:")
for user in users:
    print(user)

# Đóng kết nối
conn.close()