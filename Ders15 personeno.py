import sqlite3
menu=""""
1-kayıt
2-listele
3-sil"""
baglanti=sqlite3.connect("D://db//personelno.db")
if (baglanti):
    print("bağlntı başarılı")
else:
    print("bağlantı başarısız")
print(menu)
print("Menüden bir seçenek seçiniz")
islem_no=int(input())
if (islem_no==1):
    psno=int(input("pesonel noyu giriniz"))
    padsoy = input("pesonel adını giriniz")
    pbol=input("pesonel bolumunu giriniz")
    pma = float(input("pesonel maaşını giriniz"))
    pyil = input("pesonel yıl giriniz")
    ekle(psno,padsoy,pbol,pma,pyil)

elif (islem_no==2):

    listele()
elif(islem_no==3):
    pno=int(input("silinecek personel noyu giriniz"))
    (sil)

def listele():
    veriler=baglanti.cursor().execute("select *from kayit")
    print(veriler.fetchall())
    baglanti.commit()
    baglanti.close()
def ekle(psno,padsoy,pbol,pma,py):
    con=baglanti.cursor()
    con.execute("insert into kayit values(?????)",(psno,padsoy,pbol,pma,py))
    baglanti.commit()
    baglanti.close()
    print("kayıt yapıldı")
def sil(psno):
    baglanti.cursor()
    con.execute("Delete from kayit where =psno=?",(psno))
baglanti.commit()
baglanti.close()
print("kayıt silindi")