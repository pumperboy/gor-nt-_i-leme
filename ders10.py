# filtreleme
import cv2
import numpy as np

kamera=cv2.VideoCapture("got.mp4")

dusuk=np.array([90,50,50]) # mavi renk icin filtreleme
yuksek=np.array([130,255,255])

while True:
    red,goruntu=kamera.read()
    cv2.imshow("rgb",goruntu)
    
    hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV) # bgr uzayından hsv uzayına dönüştürdüm.
    cv2.imshow("hsv",hsv)
    
    mask=cv2.inRange(hsv,dusuk,yuksek) # belli aralıktaki renkleri beyaz yaptım.geri kalan siyah oldu.
    cv2.imshow("mask",mask)
    
    son_resim=cv2.bitwise_and(goruntu,goruntu,mask=mask)# hsv ,beyaz renk le ve lendiğinde hsv kazanır.
    cv2.imshow("renk_algilama",son_resim)
    
    #resimdeki gurulruleri azaltmak icin cesitli algoritmalar mevcut,
    # smoothed=yumusatma
    kernel=np.ones((15,15),dtype=np.float)/255
    smoothed=cv2.filter2D(son_resim,-1,kernel)
    cv2.imshow("smoothed",smoothed) 
    #blur
    blur=cv2.GaussianBlur(son_resim,(15,15),0)
    cv2.imshow("blur",blur)
    #median
    median=cv2.medianBlur(son_resim,15)
    cv2.imshow("medianblur",median)
    
    #morfolojik filtreleme
    kernel2=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel2,iterations=1)  #var olan görüntüden bir kısını siler.
    diolation=cv2.dilate(mask,kernel2,iterations=1) #var olan bütünleşik alanları birleştirip,büyütmek yada belirginleştirmek
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel2)# ayirma islemi farkli resimler daha belirgin.
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel2)# resim icindeki farklilikleri kapatir.
    
    
    cv2.imshow("erosion",erosion)
    cv2.imshow("diolation",diolation)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
      
kamera.release()
cv2.destroyAllWindows()    
'''
hsv renk uzayında parametreler birbirinden bagimsiz oldugunda filtreleme islemi kolay olur.
hue=renk degeri(0-180) araliktaki degerler ile renk belirlemeyi saglar.
saturation=doygunluk(0-255) renk'in solması yada daha belirginlesmesi
value=parlaklık resim 255 de beyazlasir 0 da siyahlasir.
'''