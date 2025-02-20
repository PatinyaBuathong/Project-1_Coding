import tkinter as tk
from tkinter import messagebox
from tkinter import font

def set_window_style(window):
    window.configure(bg="#A7C7E7")

def calculate_wv():
    try:
        w = float(entry_w.get())
        v = float(entry_v.get())
        c = (w * 100) / v
        result_wv.set(f"ความเข้มข้น: {c:.2f} g/L")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกค่าที่ถูกต้อง")

def calculate_ww():
    try:
        w1 = float(entry_w1.get())
        w2 = float(entry_w2.get())
        c = (w1 * 100) / w2
        result_ww.set(f"ความเข้มข้น: {c:.2f} g")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกค่าที่ถูกต้อง")

def calculate_molar():
    try:
        m = float(entry_m.get())
        v = float(entry_v2.get())
        c = m / v
        result_molar.set(f"ความเข้มข้น: {c:.2f} mol/L")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกค่าที่ถูกต้อง")

def create_window(title, fields, calc_function, result_var):
    window = tk.Toplevel(root)
    window.title(title)
    set_window_style(window)
    entries = []
    for field in fields:
        tk.Label(window, text=field, bg="#A7C7E7", font=("Sukhumvit Set", 14)).pack(pady=5)
        entry = tk.Entry(window, font=("Sukhumvit Set", 14))
        entry.pack(pady=5)
        entries.append(entry)
    tk.Button(window, text="คำนวณ", command=lambda: calc_function(*entries), bg="#4A90E2", fg="white", font=("Sukhumvit Set", 14, "bold"), relief="raised", borderwidth=3).pack(pady=10)
    tk.Label(window, textvariable=result_var, font=("Sukhumvit Set", 16, "bold"), bg="#A7C7E7").pack(pady=10)

def open_wv():
    global entry_w, entry_v, result_wv
    result_wv = tk.StringVar()
    create_window("คำนวณ weight/volume (g/L)", ["น้ำหนักตัวละลาย (g):", "ปริมาณสารละลาย (L):"], lambda w, v: calculate_wv(), result_wv)

def open_ww():
    global entry_w1, entry_w2, result_ww
    result_ww = tk.StringVar()
    create_window("คำนวณ weight/weight (% w/w)", ["น้ำหนักตัวละลาย (g):", "น้ำหนักของสารละลาย (g):"], lambda w1, w2: calculate_ww(), result_ww)

def open_molar():
    global entry_m, entry_v2, result_molar
    result_molar = tk.StringVar()
    create_window("คำนวณ molar (M)", ["จำนวนโมลตัวละลาย (mol):", "ปริมาตรสารละลาย (L):"], lambda m, v: calculate_molar(), result_molar)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณความเข้มข้นของสารละลาย")
root.geometry("600x450")
root.configure(bg="#A7C7E7")

header_font = font.Font(family="Sukhumvit Set", size=22, weight="bold")
sub_font = font.Font(family="Sukhumvit Set", size=14)

header_label = tk.Label(root, text="โปรแกรมคำนวณความเข้มข้นของสารละลาย", font=header_font, bg="#A7C7E7")
header_label.pack(pady=20)

frame_buttons = tk.Frame(root, bg="#A7C7E7")
frame_buttons.pack(pady=20)

button_style = {"bg": "#4A90E2", "fg": "white", "font": ("Sukhumvit Set", 16, "bold"), "relief": "raised", "borderwidth": 3, "width": 20}
tk.Button(frame_buttons, text="Weight/Volume (g/L)", command=open_wv, **button_style).pack(pady=5)
tk.Button(frame_buttons, text="Weight/Weight (% w/w)", command=open_ww, **button_style).pack(pady=5)
tk.Button(frame_buttons, text="Molar (M)", command=open_molar, **button_style).pack(pady=5)
tk.Button(frame_buttons, text="ออก", command=root.quit, bg="#D9534F", fg="white", font=("Sukhumvit Set", 16, "bold"), relief="raised", borderwidth=3, width=20).pack(pady=5)

root.mainloop()
