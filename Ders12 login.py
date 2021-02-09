
from tkinter import *

root = Tk()
root.geometry("+110+150")
root.title("login menüsü")


def kontrol():
    if ka.get() == "admin" and sifre.get() == "123":
        print("Giriş başarılı")
    else:
        print("Hata var!")


def temizle():
    ka.set("")
    sifre.set("")


f = ("Verdana", 10)
ka = StringVar()
sifre = StringVar()
alan1 = Frame(root, borderwidth=2, relief=SUNKEN ,bg="blue")
Label(alan1,text="kullanıcı adı",font=f).grid(row=2,column=3)
Label(alan1,text="Şifre",font=f).grid(row=3,column=3)
Entry(alan1,textvariable=ka,font=f).grid(row=2,column=4)
Entry(alan1,textvariable=sifre,font=f).grid(row=2,column=3)
Button(alan1,text="sil",command=temizle,font=f,).grid(row=4,column=4)
Button(alan1,text="tamam",command=kontrol,font=f,).grid(row=3,column=4)
img=PhotoImage(file="r.png")
lbl = Label(alan1, image=img)
lbl.grid(row=1, column=3, rowspan=3)
lbl["image"]=img
img1=PhotoImage(file="c.png")
lbl1 = Label(alan1, image=img)
lbl1.grid(row=2,column=0,rowspan=2)
alan1.pack(Fill=Y,expand=1)
root.mainloop()


