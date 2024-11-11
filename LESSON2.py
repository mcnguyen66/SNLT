'''
"Chủ đề: Tạo các widget cơ bản.
Kiến thức, khái niệm: Tìm hiểu về các widget cơ bản như Label, Button và Entry.
Cách sử dụng các widget này trong giao diện.
Dự án nhỏ ""Giao diện Thêm Công việc"": Tạo giao diện 
để người dùng thêm công việc với một entry và button. Học sinh sẽ học cách tạo và sử dụng các widget cơ bản."
'''
# Label, Button, Entry
# Entry Button, Widget cơ bản


import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Entry Widget Example")

# Tạo Label để hướng dẫn người dùng
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Tạo Entry để người dùng nhập tên
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Tạo Label để hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Hàm để lấy giá trị từ Entry và hiển thị
def show_name():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

# Tạo Button để gọi hàm show_name
button = tk.Button(root, text="Submit", command=show_name)
button.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()