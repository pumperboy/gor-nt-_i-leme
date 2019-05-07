import cv2
# maskeleme işlemi

resim1=cv2.imread("angelina.jpg")
resim2=cv2.imread("android.jpg")

a_gri=cv2.cvtColor(resim2,cv2.COLOR_BGR2GRAY)
cv2.imshow("griandroid",a_gri)

x,y,z=resim2.shape
bolge=resim1[0:x,0:y]
ret,mask=cv2.threshold(a_gri,10,255,cv2.THRESH_BINARY)#10 dan yüksek pixel degerini 255 yapar.(ret=10)
cv2.imshow("masklanmis",mask)

mask_inverse=cv2.bitwise_not(mask)#her pixel değerindeki renkgin, 8 lik bitteki her değeri tersine çeviri.(101=010)

angelinarka=cv2.bitwise_and(bolge,bolge,mask=mask_inverse)
# ve(and) işlemi yapıldı.0 ve 1 ler arasında, her piel deki 8 lik bitler de tek tek 2 resim karşılaştırıldı.
#beyazla resimle ve işlemi yaparsan diğer resim kazanır ,siyah la kazanırsan siyah
cv2.imshow("angelinaarka",angelinarka)

toplam=cv2.add(angelinarka,resim2)
cv2.imshow("toplam",toplam)

resim1[0:x,0:y]=toplam
cv2.imshow("yeniresim",resim1)



cv2.imshow("bolge",bolge)
cv2.imshow("griandroid",a_gri)
cv2.imshow("masklanmıis",mask)
cv2.imshow("tersmasklanmis",mask_inverse)




cv2.waitKey()
cv2.destroyAllWindows()






    