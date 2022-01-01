class Lingkaran():
    PI = 3.14
    jari_jari = 0
    luas = 0
    keliling = 0
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari 
    
    def hitungLuas(self):
        self.luas = self.PI * self.jari_jari * self.jari_jari

    def hitungKeliling(self):
        self.keliling = 2 * self.PI * self.jari_jari
    
    def cetak(self):
        print("jari-jari :", self.jari_jari)
        print("keliling :", self.keliling)
        print("luas :", self.luas)