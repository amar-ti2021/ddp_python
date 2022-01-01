class PersegiPanjang():
    panjang = 0
    lebar = 0
    luas = 0
    keliling = 0
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar 
    
    def hitungLuas(self):
        self.luas = self.panjang * self.lebar

    def hitungKeliling(self):
        self.keliling = 2 * (self.panjang + self.lebar) 
    
    def cetak(self):
        print("panjang :", self.panjang)
        print("lebar :", self.lebar)
        print("keliling :", self.keliling)
        print("luas :", self.luas)