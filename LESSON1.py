'''
# "Chủ đề: Giới thiệu về Tkinter và giao diện đồ họa.
# Kiến thức, khái niệm: Tìm hiểu về Tkinter, cài đặt và cấu trúc cơ bản của một ứng dụng Tkinter.
# Cách tạo cửa sổ chính và các thành phần giao diện cơ bản như nút, nhãn.
# Dự án ""Ứng dụng Giao diện Đầu tiên"": Tạo một ứng dụng đơn giản hiển thị một cửa sổ với nút ""Nhấn Tôi"", 
# khi nhấn vào nút sẽ hiện thông báo. Học sinh sẽ học cách sử dụng Tk() để tạo cửa sổ và Button() để tạo nút."]

pack() -> Đặt vị trí của vật theo chiều dọc hoặc chiều ngang
place() -> Đặt vị trí của label theo toạ độ x, y ---> label.place(x=100, y=100)
grid() -> Đặt vị trí của vật theo hàng và cột - > label.grid(row=0, column=0)

'''

# TKINER -> GUI
# GUI: Graphic User Interface,
#  LABER -> TEXT
# BUTTON -> CLICK SHOW # MESSAGEBOX OR LABEL

import tkinter as tk

# Create a window
root = tk.Tk()
root.title("My First GUI")
# Set size window
root.geometry("600x600")
root.configure(bg="#FFF8DE")

# Create a label

academy = tk.Label(root, text="TEKY STEAM ACADEMY", font=("Courier", 40, "bold"), fg="#D0E8C5", bg="#FFF8DE")
playlistCourses = tk.Label(root, text="Playlist Courses", font=("Tahoma", 18, "bold"), fg="#A6AEBF", bg="#FFF8DE")
courseWeb =  tk.Label(root, text="1. SIÊU NHÂN LẬP TRÌNH", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE")
courseBLG = tk.Label(root, text="2. BÉ LÀM GAME ", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE")
courseAI = tk.Label(root, text="3. PHÁT TRIỂN ỨNG DỤNG AI", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE")
courseDigiStyle = tk.Label(root, text="4. THIẾT KẾ ĐỒ HỌA", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE")
academy.pack()
playlistCourses.place(x=20, y=70)
courseWeb.place(x=30, y=100)
courseBLG.place(x=30, y=130)
courseAI.place(x=30, y=160)
courseDigiStyle.place(x=30, y=190)
# Create a button
# Create a button to show course information
showWeb = tk.Button(root, text="Info-Course", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE" )
showBLG = tk.Button(root, text="Info-Course", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE" )
showAI = tk.Button(root, text="Info-Course", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE" )
showDigistyle = tk.Button(root, text="Info-Course", font=("Tahoma", 16, "bold"), fg="#A6AEBF", bg="#FFF8DE" )
showWeb.place(x=400, y=100)
showBLG.place(x=400, y=130)
showAI.place(x=400, y=160)
showDigistyle.place(x=400, y=190)

root.mainloop() # Run the main loop