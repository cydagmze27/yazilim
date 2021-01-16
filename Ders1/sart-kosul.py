# -*- coding:utf-8 -*-
def hata():
    if kullanici!=str:
        print("Kullanıcı ismi sadece harflerden oluşur!")
           
    if parola!=int:
        print("Parola sadece rakamlardan oluşur!")
    quit

kullanici= input("Lütfen Kullanıcı adınızı giriniz:")
parola= int(input("Lütfen parolanızı giriniz:"))


if kullanici=="ceyda" and parola==123:
    print("Başarılı Giriş!")
        
else:
    hata()
    print("Lütfen kullanıcı adınızı ve parolanızı kontrol ediniz!")
    

   

