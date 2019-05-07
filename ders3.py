import cv2

resim=cv2.imread("cicek.jpg")

# resmi uzatma
uzatilan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

# resmi aynalama
aynalanan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

# resmi tekrar etme 
tekrar_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

# resmi sarma
sarma_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value=[255,0,0])

#kare secme
secme=cv2.rectangle(resim,(50,200),(200,100),[0,255,0],3) # karenin koordinatları ve çizgi renk ve kalınlığı
# sol alt ve sağ üst koordinatlar(x,y) şeklinde matris olarak düşünme,Y ÜSTTEN BAŞLAR

cv2.imshow("original",resim)
cv2.imshow("uzatma",uzatilan_resim)
cv2.imshow("aynalama",aynalanan_resim)
cv2.imshow("tekrar",tekrar_resim)
cv2.imshow("sarma",sarma_resim)
cv2.imshow("secme",secme)













cv2.waitKey(0) #resmin ekranda kalmasını sağlar.
cv2.destroyAllWindows() # daha önce açılan tüm pencereleri de kapatıyor. 



