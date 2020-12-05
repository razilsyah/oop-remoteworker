from geometri.persegi_panjang import PersegiPanjang
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

