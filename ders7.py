import cv2
import numpy as np
#saniye başına kare (fps: frame per second),FPS miktarı arttıkça görüntü daha gerçekçi ve net hale gelir
#ancak tabii ki görsel verideki bilgi miktarı da artacağı için dosyanın boyutları da artacaktır.

#0 bilgisayardan görüntü alma, 1 usb tarzı dış harici,
# video adresi koy , video oynatsın

kamera=cv2.VideoCapture("got.mkv")


while True:
    ret,kare=kamera.read()#
    #ret kameranın çalışıp çalışmadığı , ret=true,kare fotoları tutan matris
    
    bolge=kare[0:200,0:300] #video yada kameranın belli bir bölgesini alma
    cv2.rectangle(kare,(0,0),(200,200),(0,0,255),5)
    cv2.imshow("video",kare)
    cv2.imshow("bolge",bolge)
    
    if cv2.waitKey(25) & 0xFF ==ord('q'): # her 25 ms de fotograf çekiyor.q kapatma tuşu
        break
    
    

    
kamera.release()
cv2.destroyAllWindows()    
        
    
