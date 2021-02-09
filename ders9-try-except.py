birincisayi=input("Birinci sayıyı yazınız\n")
ikincisayi=input("İkinci sayıı yzınız")
try:
    sayi1=int(birincisayi)
    sayi2=int(ikincisayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")

