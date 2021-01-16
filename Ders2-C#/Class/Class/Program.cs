using System;

namespace Class
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = "CGT";
            int age = 27;

            Product product1 = new Product(); //Sınıfımızdaki 1.inci ürünümüzü ve özelliklerini belirlerdik.
            product1.ProductName = "Jacket";
            product1.ProductBrand = "Pull&Bear";
            product1.ProductModel = "Leather Jacket";
            product1.ProductSize = 36;

            Product product2 = new Product(); //Sınıfımızdaki 2.inci ürünümüzü ve özelliklerini belirlerdik.
            product2.ProductName = "Jean";
            product2.ProductBrand = "Pull&Bear";
            product2.ProductModel = "Trews";
            product2.ProductSize = 36;

            Product product3 = new Product(); //Sınıfımızdaki 3.inci ürünümüzü ve özelliklerini belirlerdik.
            product3.ProductName = "Jumper";
            product3.ProductBrand = "Pull&Bear";
            product3.ProductModel = "Turtleneck Jumper";
            product3.ProductSize = 36;

            Product[] products = new Product[] { product1, product2, product3 }; // Sınıfımızın değişkenlerini listeye atadık.

            foreach (var product in products) //Foreach döngüsüyle listemizde yer alan değişkenleri ekrana yazdırdık.
            {
                Console.WriteLine(product.ProductName + ":" + product.ProductBrand + ":" + product.ProductModel + ":" + product.ProductSize);

            }

            Console.WriteLine("The End!");
        }

    }
    class Product // Product isimli bir class oluşturduk. Çünkü birden fazla değişken tutmak istiyoruz. 
    {
        public string ProductName { get; set; } //değişkenimizin veri tipi string olduğu için string yazdık.
        public string ProductBrand { get; set; }
        public string ProductModel { get; set; }
        public int ProductSize { get; set; } //değişkenimizin veri tipi int olduğu için string yazdık.

    }

}