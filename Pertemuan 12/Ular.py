from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_Ular(self):
        super().cetak()
        print("design \t\t\t\t:", self.design,
              "\nracun \t\t\t\t:", self.racun)
              
cobra = Ular("cobra", "burung", "seluruh dunia", "bertelur", "bercorak hijau", "berbisa")
cobra.cetak_Ular()
print (" ")
sanca = Ular("sanca", "kambing", "seluruh dunia", "bertelur", "bercorak kembang", "tidak berbisa")
sanca.cetak_Ular()
print (" ")