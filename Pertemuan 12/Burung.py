from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
        self.warna = warna

    def cetak_Burung(self):
        super().cetak()
        print("jenis \t\t\t\t:", self.jenis,
              "\nbunyi \t\t\t\t:", self.bunyi,
              "\nwarna \t\t\t\t:", self.warna)
              
kakatua = Burung("kakatua", "kacang", "seluruh dunia", "bertelur", "parkit australia", "awokwok kakatua", "putih hitam")
kakatua.cetak_Burung()
print (" ")
tekukur = Burung("tekukur", "pelet", "seluruh dunia", "bertelur", "tekukur leopard", "tekukurrrr", "coklat bintik hitam")
tekukur.cetak_Burung()
print (" ")