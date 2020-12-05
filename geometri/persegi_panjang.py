class PersegiPanjang():

    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def info(self):
        print(f"objek dengan class persegipanjang , panjang = {self.panjang} lebar = {self.lebar}")


    def hitungLuas(self):
        return self.panjang * self.lebar
