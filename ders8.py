import cv2

kamera=cv2.VideoCapture("got.mkv")

kamera.set(3,400) #genislik , pixeller boyutsal büyür.(videodan belli olmuyor kameradan dene bunu)
kamera.set(4,400) #yükseklik

def ayarlama(kare,yuzde=75): #pixelleri orantısal degistirme, default 75
    genislik=int(kare.shape[1]*yuzde/100)
    yukseklik=int(kare.shape[0]*yuzde/100) # satırq
    boyut=(genislik,yukseklik)
    return cv2.resize(kare,boyut,interpolation=cv2.INTER_AREA)
    


while True:
    ret,kare=kamera.read()
    
    kare2=ayarlama(kare,50) # istedigin degeri girip kucultebilirsin
    griton=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    
    cv2.imshow("boyutlandirilmis",kare2)
    cv2.imshow("gritonda",griton)
    cv2.imshow("asil",kare) #aldığım kareleri görüntülüyorum.
    
    
    
    
    
    if cv2.waitKey(25) & 0xFF ==ord('q'): 
        break
    


kamera.release()
cv2.destroyAllWindows()    
        