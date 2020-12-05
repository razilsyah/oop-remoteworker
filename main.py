from geometri.persegi_panjang import PersegiPanjang
from geometri.pewarisan_bangunruang import BangunRuang
from geometri.segitiga import Segitiga

print("====== menggunakan OOP =======")

human1 = PersegiPanjang(10,3)
human1.info()
print(human1.hitungLuas())

print("================================================")

human2 = Segitiga(20,10)
print(human2.info())
print(human2.hitungLuas())


print("======= inheritance/pewarisan BangunRuang =========")

b1 = BangunRuang()
print(b1.info())
print(b1.hitungLuas())


# polymorphism : kemampuan objek untuk merespon berbeda ,terhadap pemanggilan method yang sama
print("======= polymorphism =======")
daftar_bangun_ruang = []
daftar_bangun_ruang.append(human1)
daftar_bangun_ruang.append(human2)

for i in daftar_bangun_ruang:
    print(i.info())