
from math import sqrt

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i].uzaklik>alist[i+1].uzaklik:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

class Nokta:
    def __init__(self, x, y,sinif):
        self.x = x
        self.y = y
        self.sinif=sinif
        
class uzaklikSinif:
     def __init__(self,uzaklik,sinif):
        self.uzaklik=uzaklik
        self.sinif=sinif

def uzaklikHesapla(dotList,yeniNokta,k):
    uzaklikListesi=[]
    for i in range(len(dotList)):
        uzaklik=uzaklikSinif(sqrt(((dotList[i].x-yeniNokta.x)**2)+((dotList[i].y-yeniNokta.y)**2)),dotList[i])
        uzaklikListesi.append(uzaklik)
    bubbleSort(uzaklikListesi)
    
    s1Sayac=0
    s2Sayac=0
    for j in range(k):
        if uzaklikListesi[j].sinif.sinif=="Sinif1":
            s1Sayac+=1
        elif uzaklikListesi[j].sinif.sinif=="Sinif2":
            s2Sayac+=1
    
    if s1Sayac>s2Sayac:
        yeniNokta.sinif="Sinif1"
    elif s2Sayac>s1Sayac:
        yeniNokta.sinif="Sinif2"
    dotList.append(yeniNokta)
    return dotList
    

k=3    
n1=Nokta(7,7,"Sinif1")
n2=Nokta(7,4,"Sinif1")
n3=Nokta(3,4,"Sinif2")
n4=Nokta(1,4,"Sinif2")
liste=[n1,n2,n3,n4]
n5=Nokta(3,7,"")
a=uzaklikHesapla(liste,n5,k)
for i in range(len(a)):
    print("x=",a[i].x,"y=",a[i].y,"Sinif=",a[i].sinif)







