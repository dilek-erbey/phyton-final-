kelime=input("Bir ifade yazınız\n \t")
kontrol="Ö,Ö,Ç,ç,Ş,ş,ı,İ"
var= False
for i in kontrol:
    if i in  kelime:
        print("Türkçe karakter kullanmayınız")
        var=True
        break
if var == False:
  print("problem yok")
