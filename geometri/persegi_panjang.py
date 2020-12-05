from geometri.pewarisan_bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):

    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def info(self):
        return f"objek dengan class persegipanjang , panjang = {self.panjang} lebar = {self.lebar}"


    def hitungLuas(self):
        return self.panjang * self.lebar
