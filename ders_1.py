import cv2

resim=cv2.imread("cicek.jpg",1) # sıfır resmi soluk renkte gösterir.bir pixelde 3 renk yerine tek renk olur.
#diğital ortamda her pixelde blue,green ve red renklerinin karışımı ile renkler oluşur.
#her rengin bir RGB değeri vardır. (BGR mantığı)
# gri tonda beyaz 0 siyah 255 
print(type(resim)) # numpy array'ine dönüştürdü.
print(resim.shape)#matris boyutunu
print(resim.size) # toplam pixel sayısı
print(resim.dtype) #8 bit den oluşur her pixel(0-255)
print(resim)
print("*********")
print(resim[50,50]) # bu değerdeki pixel in ne olduğunu gösterir.
cv2.imshow('image',resim)
#cv2.imwrite('griton.jpg',resim) # var olan dosyaya griton isminde resim dosyasını kaydetti.

cv2.waitKey(0) #resmin ekranda kalmasını sağlar.
cv2.destroyAllWindows() # daha önce açılan tüm pencereleri de kapatıyor. 


