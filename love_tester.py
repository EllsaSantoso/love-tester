import tkinter as tk
from tkinter import messagebox
import random

# Fungsi untuk menghitung kecocokan
def calculate_love():
    name1 = entry_name1.get().strip()
    name2 = entry_name2.get().strip()

    if not name1 or not name2:
        messagebox.showerror("Error", "Harap masukkan kedua nama!")
        return

    # Hitung persentase kecocokan
    compatibility = random.randint(0, 100)
    result_text = f"{name1} dan {name2} memiliki kecocokan sebesar {compatibility}%!"
    
    if compatibility > 80:
        result_text += "\n🌟 Wow, kalian pasangan serasi! 🌟"
    elif 50 <= compatibility <= 80:
        result_text += "\n😊 Hubungan kalian cukup baik, teruslah berusaha!"
    else:
        result_text += "\n😢 Mungkin kalian butuh usaha lebih untuk saling memahami."
    
    # Tampilkan hasil
    result_label.config(text=result_text)

# Membuat GUI
app = tk.Tk()
app.title("Love Tester 💞")
app.geometry("400x300")
app.resizable(False, False)

# Judul
title_label = tk.Label(app, text="Love Tester 💞", font=("tangerine", 20, "bold"), fg="#ff4d4d")
title_label.pack(pady=10)

# Input nama
frame = tk.Frame(app)
frame.pack(pady=10)

tk.Label(frame, text="Nama Anda:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
entry_name1 = tk.Entry(frame, font=("Arial", 12))
entry_name1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Nama Pasangan:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
entry_name2 = tk.Entry(frame, font=("Arial", 12))
entry_name2.grid(row=1, column=1, padx=10, pady=5)

# Tombol Hitung
test_button = tk.Button(app, text="Test My Love!", font=("Arial", 12), bg="#ff4d4d", fg="white", command=calculate_love)
test_button.pack(pady=10)

# Label Hasil
result_label = tk.Label(app, text="", font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=20)

# Jalankan aplikasi
app.mainloop()
