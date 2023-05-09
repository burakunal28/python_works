import tkinter as tk
from tkinter import messagebox
import random

fiyatlar = {
    "Çay": 10.00,
    "Kahve": 20.00,
    "Sıcak Çikolata": 30.00,
    "Kurabiye": 15.00,
    "Sandviç": 25.00,
    "Muffin": 35.00
}

def matematik_sorusu():
    sayi1 = random.randint(1, 10)
    sayi2 = random.randint(1, 10)
    islem = random.choice(["+", "-", "*", "/"])
    soru = f"{sayi1} {islem} {sayi2}"
    dogru_cevap = eval(soru)
    return soru, dogru_cevap

def soru_sor():
    global soru, dogru_cevap
    soru, dogru_cevap = matematik_sorusu()
    soru_var.set(soru)

def cevap_kontrol():
    cevap = cevap_var.get()
    if float(cevap) == dogru_cevap:
        bakiye_var.set(bakiye_var.get() + 10)
        lbl_puan["text"] = f"Puan: {bakiye_var.get()}"
        messagebox.showinfo("Doğru!", "Tebrikler, doğru cevap!")
    else:
        messagebox.showinfo("Yanlış!", "Üzgünüm, yanlış cevap.")
    cevap_var.set("")
    soru_sor()

def on_enter_key_press(event):
    cevap_kontrol()

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Çay Kahve Matik ve Matematik Oyunu ve Kafe")

# Pencere boyutu ve konumu
pencere_width = 400
pencere_height = 600
ekran_width = pencere.winfo_screenwidth()
ekran_height = pencere.winfo_screenheight()
x = (ekran_width // 2) - (pencere_width // 2)
y = (ekran_height // 2) - (pencere_height // 2)
pencere.geometry(f"{pencere_width}x{pencere_height}+{x}+{y}")

# Matematik oyunu
soru_var = tk.StringVar()
lbl_soru = tk.Label(pencere, textvariable=soru_var, font=("Arial", 16))
lbl_soru.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
soru_sor()

cevap_var = tk.StringVar()
entry_cevap = tk.Entry(pencere, textvariable=cevap_var, font=("Arial", 16))
entry_cevap.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
entry_cevap.bind("<Return>", on_enter_key_press)

btn_cevap = tk.Button(pencere, text="Cevapla", command=cevap_kontrol)
btn_cevap.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Puan
bakiye_var = tk.DoubleVar()
bakiye_var.set(0)
lbl_puan = tk.Label(pencere, text=f"Puan: {bakiye_var.get()}", font=("Arial", 16))
lbl_puan.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")

# Ürün düğmeleri
btn_cay = tk.Button(pencere, text="Çay\n10.00 TL", command=lambda: siparis_ekle("Çay"), font=("Arial", 16))
btn_cay.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

btn_kahve = tk.Button(pencere, text="Kahve\n20.00 TL", command=lambda: siparis_ekle("Kahve"), font=("Arial", 16))
btn_kahve.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

btn_sicak_cikolata = tk.Button(pencere, text="Sıcak Çikolata\n30.00 TL", command=lambda: siparis_ekle("Sıcak Çikolata"), font=("Arial", 16))
btn_sicak_cikolata.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

btn_kurabiye = tk.Button(pencere, text="Kurabiye\n15.00 TL", command=lambda: siparis_ekle("Kurabiye"), font=("Arial", 16))
btn_kurabiye.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

btn_sandvic = tk.Button(pencere, text="Sandviç\n25.00 TL", command=lambda: siparis_ekle("Sandviç"), font=("Arial", 16))
btn_sandvic.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

btn_muffin = tk.Button(pencere, text="Muffin\n35.00 TL", command=lambda: siparis_ekle("Muffin"), font=("Arial", 16))
btn_muffin.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

# Siparişler
lst_siparisler = tk.Listbox(pencere, font=("Arial", 16))
lst_siparisler.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

toplam_tutar = 0.0
lbl_toplam_tutar = tk.Label(pencere, text=f"Toplam Tutar: {toplam_tutar} TL", font=("Arial", 16))
lbl_toplam_tutar.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="e")

# Yardım
def yardim():
    messagebox.showinfo("Yardım", "Bu uygulama ile matematik oyunu oynayabilir ve bir kafede sipariş verebilirsiniz. Siparişlerinizi sepete ekleyebilir, siparişleri silebilir ve toplam tutarı görüntüleyebilirsiniz.")

menubar = tk.Menu(pencere)
yardim_menu = tk.Menu(menubar, tearoff=0)
yardim_menu.add_command(label="Yardım", command=yardim)
menubar.add_cascade(label="Yardım", menu=yardim_menu)
pencere.config(menu=menubar)

def siparis_ekle(urun):
    global toplam_tutar
    fiyat = fiyatlar[urun]
    toplam_tutar += fiyat
    lst_siparisler.insert(tk.END, f"{urun} - {fiyat:.2f} TL")
    lbl_toplam_tutar["text"] = f"Toplam Tutar: {toplam_tutar:.2f} TL"

# Hücre boyutlarını ayarla (responsive)
for i in range(8):
    tk.Grid.rowconfigure(pencere, i, weight=1)
tk.Grid.columnconfigure(pencere, 0, weight=1)
tk.Grid.columnconfigure(pencere, 1, weight=1)

# Ana döngüyü çalıştır
pencere.mainloop()