import numpy as np
from PIL import ImageGrab
import cv2
from os import listdir
from os.path import isfile, join
import calculate
from calculate import Calculate
import time
import threading, queue
import logging



q=queue.Queue()
class Convert():
    #------testing
    #mynum=0
    #-------testing
    onlyfiles = [f for f in listdir("C:/Users/enisk/Desktop/Yeni klasör/Test/pictures") if isfile(join("C:/Users/enisk/Desktop/Yeni klasör/Test/pictures", f))]
    onlyfiles.remove("calculate.py")
    onlyfiles.remove("convert.py")
    #------testing ==> reversetake ile entegre kullanmak için
    #mynum1=len(onlyfiles)
    #------testing
    def  __init__(self):
        threading.Thread.__init__(self)

    @classmethod
    def take(cls):
        
        while True:
            item=q.get()
            
            logging.warning("\n %s. %s içerisinde;\n",(item +1),"resim")
            calculate.Calculate(cv2.cvtColor(cv2.imread(cls.onlyfiles[item]),cv2.COLOR_BGR2GRAY))
            #-----------------Testing
            #cls.mynum+=1
            #-----------------Testing
            q.task_done()
            
            
            
    #-----------------Testing
    @classmethod
    def reversetake(cls):        
        reverseiter=iter(cls.onlyfiles[::-1])
        while not cls.mynum==cls.mynum1:
            
            logging.warning("\n %s. %s içerisinde;\n",(cls.mynum1),"resim")
            calculate.Calculate(cv2.cvtColor(cv2.imread(next(reverseiter)),cv2.COLOR_BGR2GRAY))
            cls.mynum1-=1

    #-----------------Testing

    


def run():        

    pictures = "C:/Users/enisk/Desktop/Yeni klasör/Test/pictures"

    onlyfiles = [f for f in listdir("C:/Users/enisk/Desktop/Yeni klasör/Test/pictures") if isfile(join("C:/Users/enisk/Desktop/Yeni klasör/Test/pictures", f))]
    onlyfiles.remove("calculate.py")
    onlyfiles.remove("convert.py")

    print(onlyfiles)
    print(len(onlyfiles))
    print(onlyfiles[0])
    print(range(len(onlyfiles)-1))
    threading.Thread(target=Convert.take, daemon=True).start()


    for item in range(len(onlyfiles)):
        q.put(item)    
    q.join() 

run()


def info():
    print("################  BİLGİLER  ##########################")
        
    print(threading.active_count(),"çalışan threadler")
    print("3")
    print(threading.current_thread(),"kontrol dizesine karşılık gelen iş parçacığı")
    print("4")
    print(threading.main_thread(),"Ana iş parçacığı (main-thread) nesnesi")        

info()

#with open("Sonuçlar.txt","w") as son:
#   son.write(f"{i} içerisinde;")


#if cls.onlyfiles[item]=="sample3.jpg":
#   continue