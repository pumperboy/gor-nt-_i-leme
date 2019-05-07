import cv2
#aynı pixel boyutundaki resimler toplanır.

def main():
    resim1=cv2.imread("tel1.jpg")
    resim2=cv2.imread("tel2.jpg")
    
    print(resim1[100,100])
    print(resim2[100,100])
    print(resim1[100,100]+resim2[100,100]) # 8 bitlik toplama işlemi
    print(cv2.add(resim1[100,100],resim2[100,100])) #doygunluğa ulaştı.tek bir nokta için
    
    toplam=cv2.add(resim1,resim2)
    agirlikli_toplam=cv2.addWeighted(resim1,0.8,resim2,0.2,0)# her pixel i verilen oranlarla çarpar.
    
    cv2.imshow("bir",resim1)
    cv2.imshow("iki",resim2)
    cv2.imshow("toplam",toplam)
    cv2.imshow("agirlik",agirlikli_toplam)
    
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    
    
    
    
if __name__== "__main__":
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
