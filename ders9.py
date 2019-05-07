import cv2


kamera=cv2.VideoCapture("got.mkv")
fourcc=cv2.VideoWriter_fourcc(*"XVID") # format
kayit=cv2.VideoWriter("kayit.mkv",fourcc,30,(640,480)) # 30 fbs ve boyut

while True:
    ret,kare=kamera.read()
    
    ters_kare=cv2.flip(kare,0)
    
    if ret==True:  # kamera çalıştıkca kaydeder.
        kayit.write(kare) # ters_kare yaz  onu kaydeder.
    
    
    cv2.imshow("asil",kare) 
    
    
    if cv2.waitKey(25) & 0xFF ==ord('q'): 
        break
    
kamera.release()
cv2.destroyAllWindows()    
            




