import math
class SegitigaSiku2():
    alas = 0
    tinggi = 0
    luas = 0
    keliling = 0
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi 
    
    def hitungLuas(self):
        self.luas = 0.5 * self.alas * self.tinggi

    def hitungKeliling(self):
        sisi_miring = self.alas**2 + self.tinggi**2
        sisi_miring = math.sqrt(sisi_miring)        
        self.keliling = self.alas + self.tinggi + sisi_miring
    
    def cetak(self):
        print("alas :", self.alas)
        print("tinggi :", self.tinggi)
        print("keliling :", self.keliling)
        print("luas :", self.luas)
