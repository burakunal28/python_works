import tkinter
from tkinter import *

pencere = Tk() #Tk bir tkinter sınıfıdır
pencere.geometry("300x500")
pencere.title("Hesap Makinesi")
pencere.config(background="#282828", padx=5, pady=5)

def toplama():
    sonuc_box.configure(state=NORMAL)
    sayi1=int(say1.get())
    sayi2=int(say2.get())
    sonuc_toplama=sayi1+sayi2
    sonuc_box.insert(END, str(sonuc_toplama))
    sonuc3.config(text=sonuc_toplama)
    sonuc_box.configure(state=DISABLED)

def cikarma():
    sonuc_box.configure(state=NORMAL)
    sayi1=int(say1.get())
    sayi2=int(say2.get())
    sonuc_cikarma=sayi1-sayi2
    sonuc_box.insert(END, str(sonuc_cikarma))
    sonuc3.config(text=sonuc_cikarma)
    sonuc_box.configure(state=DISABLED)

def carpma():
    sonuc_box.configure(state=NORMAL)
    sayi1=int(say1.get())
    sayi2=int(say2.get())
    sonuc_carpma=sayi1*sayi2
    sonuc_box.insert(END, str(sonuc_carpma))
    sonuc3.config(text=sonuc_carpma)
    sonuc_box.configure(state=DISABLED)

def bolme():
    sonuc_box.configure(state=NORMAL)
    sayi1=int(say1.get())
    sayi2=int(say2.get())
    sonuc_bolme=sayi1//sayi2
    sonuc_box.insert(END, str(sonuc_bolme))
    sonuc3.config(text=sonuc_bolme)
    sonuc_box.configure(state=DISABLED)

def temizle():
    sonuc_box.configure(state=NORMAL)
    sonuc_box.delete(0,END)
    sonuc_box.configure(state=DISABLED)
    sonuc3.config(text=0)

baslik=Label(text="Hesap Makinesi")
baslik.place(x=90, y=10)

metin1=Label(text="1. Sayı:", fg="#efefef", bg="#282828")
metin1.place(x=10, y=40)

say1=Entry(width=15)
say1.place(x=120, y=40)

metin2=Label(text="2. Sayı:", fg="#efefef", bg="#282828")
metin2.place(x=10, y=80)

say2=Entry(width=15)
say2.place(x=120, y=80)

topla=Button(text="Topla", width=20, command=toplama)
topla.place(x=15, y=120)

cikart=Button(text="Çıkart", width=20, command=cikarma)
cikart.place(x=15, y=160)

carp=Button(text="Çarp", width=20, command=carpma)
carp.place(x=15, y=200)

bol=Button(text="Böl", width=20, command=bolme)
bol.place(x=15, y=240)

temizle_buton=Button(text="Temizle", width=20, command=temizle)
temizle_buton.place(x=15, y=280)

sonuc=Label(text="Sonuç 1:")
sonuc.place(x=30, y=320)

sonuc_box=Entry(width=10)
sonuc_box.configure(state=DISABLED)
sonuc_box.place(x=100, y=320)

sonuc2=Label(text="Sonuç 2:")
sonuc2.place(x=30, y=360)

sonuc3=Label(text="0", width=10)
sonuc3.place(x=100, y=360)

mainloop()
