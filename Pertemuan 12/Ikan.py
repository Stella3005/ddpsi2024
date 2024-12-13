from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna

    def cetak_Ikan(self):
        super().cetak()
        print("jenis \t\t\t\t:", self.jenis,
              "\nwarna \t\t\t\t:", self.warna)
              
arwana = Ikan("arwana", "serangga", "aquarium", "bertelur", "super red", "merah")
arwana.cetak_Ikan()
print (" ")
cupang = Ikan("cupang", "jentik jentik", "aquarium", "bertelur", "betta smaragdina", "hijau gradasi hitam")
cupang.cetak_Ikan()
print (" ")