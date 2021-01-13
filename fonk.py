def kullanici_dogrulugu():
    if kullanici=="ceyda" and parola==123:
        print("Başarılı Giriş!")
        
    else:
        print("Lütfen kullanıcı adınızı ve parolanızı kontrol ediniz!")
        quit()
        
def kullanici_sec():
    if isinstance(kullanici,str)==True:
        print("İşlem Başarılı!")
    else:
        quit()

def parola_sec():
    if isinstance(parola,int)==True:
        print("İşlem Başarılı!")
    else:
        quit()

kullanici= input("Lütfen Kullanıcı adınızı giriniz:")
parola= int(input("Lütfen parolanızı giriniz:"))


kullanici_dogrulugu()  
