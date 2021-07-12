import time
print("*********************************\n"
      "Para Bank ATM ' ye Hoşgeldiniz!!\n"
      "İşlemler : \n"
      "1.Bakiye Sorgulama\n"
      "2.Para Yatırma\n"
      "3.Para Çekme\n"
      "4.Ödeme Yap \n"
      "5.Kredi Sorgulama\n"
      "6.Kredi Çek\n"
      "Programdan çıkmak için 'q' ya basın.\n"
      "********************************\n")
bakiye= 3000
kredi = 10000
while True:
    islem=input("İşlem Seçin:")
    if(islem=="q"):
        print("Çıkış yapılıyor..")
        time.sleep(1)
        print("Çıkış yapıldı. Bizi tercih ettiğiniz için teşekküler")
        break
    elif(islem=="1"):
        print("Bakiyeniz : {} TL".format(bakiye))
    elif(islem=="2"):
        miktar=int(input("Yatırmak istediğiniz miktar : "))
        print("Para yatırılıyor.")
        time.sleep(1)
        bakiye+=miktar
        print("Para yatırıldı.")
    elif(islem=="3"):
        miktar=int(input("Çekmek istediğiniz miktar: "))
        if(bakiye-miktar<0):
            print("Bakiye yeteriz!!")
        else:
            time.sleep(1)
            bakiye-=miktar
            print("Ödemeniz yapıldı. Tekrar bekleriz")
    elif(islem=="4"):
        miktar=int(input("Ödeme yapmak istediğiniz miktar:"))
        if(bakiye-miktar<0):
            print("Ödeme yapmak için yeterli bakiyeniz yok !!")
        else:
            time.sleep(1)
            bakiye-=miktar
            print("Ödemenize yapıldı. Tekrar bekleriz.")
    elif(islem=="5"):
        print("Maksimum {} TL'ye kadar kredi çekebilirsiniz.".format(kredi))
    elif(islem=="6"):
        miktar=int(input("Çekmek istediğiniz kredi miktarı :"))
        if(kredi-miktar<0):
            print("Kredi bakiyeniz yetersiz!!!")
        else:
            kredi-=miktar
            bakiye+=miktar
            time.sleep(1)
            print("İşleminiz gerçekleşti. Tekrar bekleriz")
    else:
        print("Geçersiz işlem yaptınız")



