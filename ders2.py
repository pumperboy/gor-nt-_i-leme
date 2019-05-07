import cv2

resim=cv2.imread("angelina.jpg",1)#resmi numpy array sınıfına dönüştürdü.
resim2=cv2.imread("cicek.jpg",0)
resim3=cv2.imread("angelina.jpg",0)
print(resim.shape)

#for i in range(200):
#    resim[200,i]=[250,250,250]
bölge=resim[100:300,200:500]
cv2.imshow("yenibolge",bölge)

resim[100:300,200:500,2]=255 # sırayla b g r = [0,1,2]
cv2.imshow("sevgili",resim)

print("****************************")
# resim taşıma 
size=resim2.shape
resim3[:201,:251]=0
cv2.imshow("yeniden",resim3)
resim3[:201,:251]=resim2
cv2.imshow("yeniresim",resim3)


cv2.waitKey(0)
cv2.destroyAllWindows()