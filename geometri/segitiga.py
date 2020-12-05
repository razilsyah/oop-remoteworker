class Segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi


    def info(self):
        return f"ini adalah objek dengan class segitiga , alas = {self.alas} tinggi = {self.tinggi}"


    def hitungLuas(self):
        return self.alas * self.tinggi / 2