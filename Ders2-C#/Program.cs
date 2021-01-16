using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            //type safety - tip güvenliği
            string kategoriEtiketi = "Kategoriler";
            int ogrenciSayisi = 32000;
            double faizOrani = 1.45;
            bool sistemeGirisYapmisMi = true;

            if (sistemeGirisYapmisMi == true)
            {
                Console.WriteLine("Kullanıcı ayarları butonu");
            }
            else
            {
                Console.WriteLine("Giriş yap butonu")
            }
        }
    }
}
