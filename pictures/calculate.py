import numpy as np
from PIL import ImageGrab
import cv2



class Calculate():

    def __init__(self,thread):
        self.thread=thread
        self.find(self.thread)

    

        
    def find(self,thread): 
        OrnekResim = cv2.imread('sample3.jpg') #Tespit Edeceğimiz Resim
        OrnekResimDonustur = cv2.cvtColor(OrnekResim,cv2.COLOR_BGR2GRAY) #Tespit Edeceğimiz Resimi Gri Formata Donustur 
        Sonuc =	cv2.matchTemplate(self.thread,OrnekResimDonustur,cv2.TM_CCOEFF_NORMED)
        #Ekran Grountusunun Icerisinde Resmi Ariyoruz
        sin_val,max_val,min_loc,max_loc = cv2.minMaxLoc(Sonuc) #Bulunan Objenin Koordinatlarini Bul
        Ust_Sol = max_loc #Bulunan Objenin Ust ve Sol Uzakligi
        Alt_Sag = (Ust_Sol[0]+50, Ust_Sol[1]+50) #Bulunan Objenin Alt ve Sag Uzakligi
        cv2.rectangle(self.thread, Ust_Sol, Alt_Sag, (0,255,0),5) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle
        mycalc=int(len(max_loc)//2)
        cv2.imshow('ARABA KONUMLARI!',self.thread) #Ekran Goruntusunu Goster

        
        if mycalc==0:
            self.sonuc="Hiç Araç Bulunmadı!"
            print(self.sonuc)


        else:
            
            self.sonuc=f"{str(mycalc)}' araç bulundu!"
            with open("Sonuçlar.txt","a") as son:
                son.write(self.sonuc)
            print(self.sonuc)





        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            quit()

        
        



