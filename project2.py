# class Telephone:
#     def __init__(self,model,price,storage):
#         self.model = model
#         self.price = price
#         self.storage = storage
#     def get_info(self):
#         return f"Modelimiz: {self.model}, Narxi: {self.price}, Xotirasi: {self.storage}"
#     def call(self,raqam):
#         return f"{raqam}ga telefon qiling"
#
# a = Telephone("Samsung","1000","512")
# b = Telephone("Iphone","2000","256")
# print(a.get_info())
# print(b.call(input("Raqam kiriting: ")))

# class Computer:
#     def __init__(self,model,price,storage):
#         self.model = model
#         self.price = price
#         self.storage = storage
#     def get_info(self):
#         return f"Modelimiz: {self.model}, Narxi: {self.price}, Xotirasi: {self.storage}"
#     def call(self,raqam):
#         return f"{raqam}ga telefon qiling"
# a = Computer("HP","500","512")
# b = Computer("Asus","300","512")
# print(a.get_info())
# print(b.get_info())
# print(b.call(input("Raqam kiriting: ")))

# class Game:
#     def __init__(self,name,strength,life):
#         self.name = name
#         self.strength = strength
#         self.life = life
#     def attack(self):
#         if self.life<100:
#             return f"Ismiz: {self.name}, Kuchingiz: {self.strength}, Joningiz: {self.life}"
#         else:
#             return f"100dan katta bulmasligi kerak"
# a = Game("Nabi","1000","50")
# print(a.attack())
#1
# class Inson:
#     def __init__(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh
# class Oqituvchi(Inson):
#     def __init__(self,ism,yosh,fan):
#         super().__init__(ism, yosh)
#         self.fan = fan
#     def tanishuv(self):
#         return f"Men {self.ism}, {self.yosh} yoshdaman. Men {self.fan} fandan o'taman."
# class Oquvchi(Inson):
#     def __init__(self,ism,yosh,sinf):
#         super().__init__(ism,yosh)
#         self.sinf = sinf
#3
# class Tanishtiruv:
#     def tanishtir(self):
#         return f"Salom mening ismim Diyora"
# class Salom:
#     def tanishtir(self):
#         return f"Bu mening oilam"
# class Alik:
#     def tanishtir(self):
#         return f"Bu mening dostlarim"
# for Tanishtiruv in [Tanishtiruv(),Salom(),Alik()]:
#     print(Tanishtiruv.tanishtir())
# class Tanishtiruv:
#     def tanishtir(self):
#         return f"Salom mening ismim shu"
# class Salom:
#     def tanishtir(self):
#         return f"Bu mening dostlarim"
# class Alik:
#     def tanishtir(self):
#         return f"Bu mening oilam"
# for Tanishtiruv in [Tanishtiruv(),Salom(),Alik()]:
#     print(Tanishtiruv.tanishtir())

# class Hayvon:
#     def __init__(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh
#
# class It(Hayvon):
#     def __init__(self,ism,yosh):
#         super.__init__(ism,yosh)
#
#     def ovoz(self):
#         return "Vov-vov"
# class Qush(Hayvon):
#    def __init__(self,ism,yosh):
#        super.__init__(ism,yosh)
#
#     def ovoz(self):
#         return "Chirq-chirq"
#
# it = It("Rex", 3)
# qush = Qush("Kesha", 2)
# print(it.ism, it.yosh)
# print(it.ovoz())
# print(qush.ism, qush.yosh)
# print(qush.ovoz())

# class Ona:
#     def ovoz(self):
#         return "Nimaa"
#
# class farzand1(Ona):
#     def ovoz(self):
#         return "Oyijon"
#
# class farzand2(Ona):
#     def ovoz(self):
#         return "Onajon"
#
# for ona in [farzand1(), farzand2(), Ona()]:
#     print(ona.ovoz())

# class Hayvon:
#     def __init__(self, ism):
#         self.ism = ism
#         self.__jon = 100
#
#     def jon_holati(self):
#         return self.__jon
#
#     def ovqatlantir(self):
#         self.__jon += 10
#
#         if self.__jon > 100:
#             self.__jon = 100
# hayvon = Hayvon("Rex")
# print(hayvon.jon_holati())
# hayvon.ovqatlantir()

# print(hayvon.jon_holati())
#1
# import logging
# logging.basicConfig(filename="jurnal.log",filemode="a",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")
# class Xona:
#     jami = 0
#     def __init__(self,raqam,narx,sigim=2):
#         self.raqam = raqam
#         self.narx = narx
#         self.sigim = sigim
#         self.__band = []
#         Xona.jami += 1
#         logging.info(f"Xona yaratildi: {self.raqam}")
#     def band_qilish(self,ism):
#         if len(self.__band) < self.sigim:
#             self.__band.append(ism)
#             logging.info(f"{ism} {self.raqam}-xonani band qildi")
#         else:
#             logging.warning(f"{self.raqam}-xona to'la")
#     def bekor_qilish(self,ism):
#         if ism in self.__band:
#             self.__band.remove(ism)
#             logging.info(f"{ism} bronni bekor qildi")
#         else:
#             logging.error(f"{ism} bron topilmadi")
#     def __str__(self):
#         return f"Xona: {self.raqam} Narxi: {self.narx} Band: {self.__band}"
# xona1= Xona(101,200000)
# xona1.band_qilish("Ali")
# xona1.band_qilish("Vali")
# xona1.band_qilish("Sardor")
#
# xona1.bekor_qilish("Ali")
# xona1.bekor_qilish("Hasan")
#2
# with open("jurnal.log", "r") as f:
#     info = 0
#     warning = 0
#     error = 0
#     for i in f:
#         if "INFO" in i:
#             info += 1
#         if "WARNING" in i:
#             warning += 1
#         if "ERROR" in i:
#             error += 1
# print(f"INFO: {info}")
# print(f"WARNING: {warning}")
# print(f"ERROR: {error}")
#3
# import logging
# logging.basicConfig(level=logging.ERROR,format='%(levelname)s: %(message)s')
#
# logging.info("A")
# logging.warning("B")
# logging.error("C")
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("D")
# logging.critical("E")

