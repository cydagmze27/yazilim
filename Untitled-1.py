def kullanici_dogrulugu():
    if kullanici=="ceyda" and parola==123:
        print("Başarılı Giriş!")
        
    else:
        print("Lütfen kullanıcı adınızı ve parolanızı kontrol ediniz!")

def hata():
    if kullanici!=str():
        print("Kullanıcı ismi sadece harflerden oluşur!")
           
    if parola!=int():
        print("Parola sadece rakamlardan oluşur!")
    quit

kullanici= input("Lütfen Kullanıcı adınızı giriniz:")
parola= int(input("Lütfen parolanızı giriniz:"))

kullanici_dogrulugu()
hata()

   

 