"""r= dosyayı sadece okumak için aç
r+ hem okuma hem yazmak
a dosyayı ekleme için açar
a+ hem eklem hem okuma"""
from sys import argv
program,dosya=argv
metin1=open(dosya)
print ("dosyamızın içeriği aşağıdaki gibidir:")%dosya
icerik=metin1.read()
print(icerik)
metin1=open(dosya,'w')
metin1.truncate()
print("kitap adı:")
yenibilgi=input("kitap adını yazınız")
metin1.write((yenibilgi+"\n")*4+yenibilgi)
print ("kitap adı: %r" % (metin1))
metin1.close()

open(dosya).read()
metin2=open('yedek'+dosya,'w')
metin2.write(icerik)
metin2.close()
print("dosyanızın yedeği kaydedilmiştir")

