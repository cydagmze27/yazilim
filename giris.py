sayilar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def kullaniciAl():
    while True:
        kullanici= input("Lütfen kullanıcı adınızı giriniz: ")
        kontrol = False
        i = 0
        while i < len(sayilar):
            if sayilar[i] in kullanici:
                kontrol = True
                break
            i += 1
            
        if kontrol == False:
            # yani içinde sayı yok demektir.
            break
        else:
            print('Kullanıcı adı yalnızca harflerden oluşmalıdır!')
            
    sifreAl(kullanici)
        
def sifreAl(kullanici):
    while True:
        sifre = input("Lütfen şifrenizi giriniz: ")
            
        if sifre.isnumeric():
            # yani içinde harf yok demektir.
            break
        else:
            print('Şifre yalnızca rakamlardan oluşmalıdır!')
            
    kontrolEt(kullanici, sifre)
            
def kontrolEt(kullanici, sifre):
    
    if ( kullanici == 'ceyda' and sifre == '123' ):
        print('Giriş başarılı. 🥳')
    else:
        print("Lütfen kullanıcı adı ve şifre alanlarını kontrol ediniz!")

kullaniciAl()