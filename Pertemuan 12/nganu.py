class Person:
    def __init__(self, nama, umur, jekel):
        self.nama = nama
        self.umur = umur
        self.jekel = jekel

    def jalan(self):
        print (f"{self.nama}bisa berjalan")

    def ngomong(self):
        print(f"dia berbicara karena dia{self.jekel}")

class Supir(Person):
    def __init__(self, nama, umur, jekel, sim):
        super().__init__(nama, umur, jekel)
        self.sim = sim

    def nyupir(self):
        print(f"{self.nama} bisa nyupir karena memiliki sim {self.sim}")

class Mahasiswa(Person):
    def __init__(self, nama, umur, jekel, nim):
        super().__init__(nama, umur, jekel)
        self.nim = nim

bayu = Person("bayu", 20, "laki laki")
bayu.jalan()
bayu.ngomong()

andi = Supir("andi", 30, "laki laki", "A")
andi.nyupir()

bunga = Mahasiswa("bunga", 21, "Perempuan", "nim")