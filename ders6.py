import cv2
import numpy as np

resim=cv2.imread("android.jpg")

ikikat=cv2.pyrUp(resim)# 2 kat büyüdü ,çıktıda bak
ikikat_kucul=cv2.pyrDown(resim)#2 kat küçüldü
cv2.imshow("degisen",ikikat)
cv2.imshow("asil",resim)

resim2=np.zeros((400,400,3),dtype="uint8")# siyah bir resim oluşur.


resim2.fill(255) # resim içindeki tüm pixelleri 255 yapar.tek argüman alır

cv2.line(resim2,(0,0),(200,200),(255,0,0),3) # düz çizgi çeker
cv2.circle(resim2,(200,200),50,(0,255,0),3)# yarıçapı 50 olan çember
cv2.putText(resim2,"ahmet baspinar",(150,150),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),3)# başlama noktası,yazı tipi
# yazı boyut ,reng, kalınlığı  


cv2.imshow("siyah ekran",resim2)























cv2.waitKey()
cv2.destroyAllWindows()
