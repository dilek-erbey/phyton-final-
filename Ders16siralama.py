dizi=[6,3,45,2,10]
def secim(dizi):
    for i in range (len(dizi)):
        min_index =i
        for j in range(i+1,len(dizi)):
            if dizi[min_index]> dizi[j]:
                min_index=j
        if min_index !=i:
          dizi[i],dizi[min_index]=dizi[min_index],dizi[i]
          print(dizi)

secim(dizi)
