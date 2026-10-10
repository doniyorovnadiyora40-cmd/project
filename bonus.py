# products={}
#
# def add_product():
#     name = input("Mahsulot nomi: ")
#     if name in products:
#         print("Bu mahsulot allaqachon mavjud!")
#         return
#     narx = int(input("Narxi (so'm): "))
#     soni = int(input("Soni (dona): "))
#     products[name] = {"narx": narx, "soni": soni}
#     print(f"{name} omborga qo'shildi!")
#
# def all_product():
#     if not products:
#         print("Ombor bo'sh!")
#         return
#
#     for key,value in products.items():
#         print(f"----------------------------------------\n"
#               f"MAHSULOT             NARXI     SONI \n"
#               f"----------------------------------------\n"
#               f"{key}                 {value['narx']}       {value['soni']}\n"
#               f"----------------------------------------\n"
#               f"Jami: {len(products)} xil mahsulot")
#
# def search_product():
#     name=input("Qaysi mahsulotni qidiramiz? ").lower()
#     if name in products:
#         print(f"{name}: narxi {products[name]["narx"]} so'm, omborda {products[name]["soni"]} dona")
#     else:
#         print(f"{name} omborda topilmadi!")
# def update_product():
#     name=input("Qaysi mahsulotni yangilaymiz? ").lower()
#     if name not in products:
#         print(f"{name} omborda yo'q")
#     else:
#         print(f"1 - Kirim(soni oshadi)\n2 - Chiqim(soni kamayadi)\n3 - Yangi narx")
#         choice=input("Tanlang: ")
#         if choice=="1":
#             miqdor=int(input("Nechta keldi: "))
#             a=products[name]["soni"]+miqdor
#             print(f"Kirim qabul qilindi. Endi {name}: {a} dona")
#         elif choice=="2":
#             miqdor = int(input("Nechta chiqdi? "))
#             if miqdor > products[name]["soni"]:
#                 print("Omborda buncha mahsulot yo'q!")
#             else:
#                 a=products[name]["soni"] - miqdor
#                 print(f"Chiqim bajarildi! Qoldi: {a} dona")
#         elif choice == "3":
#             yangi_narx = float(input("Yangi narx: "))
#             products[name]["narxi"] = yangi_narx
#             print(f"{name} narxi yangilandi! {yangi_narx} so'm")
#         else:
#             print("Bunday bo'lim yo'q!")
#
# def delete_product():
#     name = input("Qaysi mahsulotni o'chiramiz? ").lower()
#     if name not in products:
#         print(f"{name} omborda yo'q.")
#         return
#     a=input(f"{name} rostdan o'chirilsinmi? (ha/yoq): ").lower()
#     if a.lower()=="ha":
#         del products[name]
#         print(f"{name} ombordan o'chirildi!")
#     else:
#         print("Bekor qilindi.")
# def all_amount():
#     all=0
#     for key,value in products.items():
#         all+=value["narx"]*value["soni"]
#     print(f"Ombordagi jami boylik: {all} so'm")
#
# def main():
#     print("""
# ========================================
#         OMBORXONA TIZIMI v1.0
# ========================================""")
#     while True:
#         tanlov=input("""
# 1 — Mahsulot qo'shish
# 2 — Barcha mahsulotlar
# 3 — Qidirish
# 4 — Yangilash (kirim/chiqim/narx)
# 5 — O'chirish
# 6 — Umumiy qiymat
# 0 — Chiqish
# >>> Bo'limni tanlang: """)
#         if tanlov == "1":
#             add_product()
#         elif tanlov=="2":
#             all_product()
#         elif tanlov=="3":
#             search_product()
#         elif tanlov=="4":
#             update_product()
#         elif tanlov=="5":
#             delete_product()
#         elif tanlov=="6":
#             all_amount()
#         elif tanlov=="0":
#             print("Dastur tugadi.Xayr!")
#             break
#         else:
#             print("Bunday bo'lim yo'q. Qaytadan tanlang.")
# main()
#1
# class Bank:
#     jami = 0
#     def __init__(self,egasi,balans=0):
#         self.egasi = egasi
#         self.__balans = balans
#         Bank.jami += 1
#     @property
#     def balans(self):
#         return self.__balans
#     @balans.setter
#     def balans(self,qiymat):
#         if qiymat < 0:
#             raise ValueError("Balans manfiy bo'lishi mumkin emas.")
#         self.__balans = qiymat
# #2
#     @classmethod
#     def hisoblar_soni(cls):
#         return cls.jami
# #3
#     @staticmethod
#     def valyuta_kursi(usd):
#         kurs = 12000
#         return usd * kurs
# #4
#     def __str__(self):
#         return f"Hisob egasi: {self.egasi}\nBalans: {self.balans} so'm"
#     def __eq__(self, other):
#         return self.balans == other.balans
#     def __gt__(self, other):
#         return self.balans > other.balans
#     def __add__(self, other):
#         yangi = self.balans + other.balans
#         return f"{self.egasi} + {other.egasi}\n {yangi}"
# #5
# acc1 = Bank("Ali",5000000)
# acc2 = Bank("Vali",6000000)
# acc3 = Bank("G'ani",7000000)
# print(acc1)
# print(acc1.balans)
# acc1.balans = 75000000
# print(acc1.balans)
# print(acc1==acc2)
# print(acc1>acc2)
# print(Bank.hisoblar_soni())
# usd=100
# print(Bank.valyuta_kursi(usd))
# new = acc1 + acc2
# print(new)



# @decorator
import  time
# def taymer(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#
#
#         return result
#     return wrapper
#
# @taymer
# def sekin_funksiya():
#     for i in range(10_000_000):
#         pass
# taymer(sekin_funksiya)


# def ikki_marta(func):
#     def wrapper(*args, **kwargs):
#         x = func(*args, **kwargs)
#
#         return x*x
#     return wrapper
#
# @ikki_marta
# def salom_ber(name):
#     return f"salom {name}"
#
# print(salom_ber("Ali"))

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
# @decor1
# @decor
# def num():
#     return 10
# print(num())
# print(num2())
#2
# import requests
# import json
# from datetime import date
#
# def kurslarni_olish():
#     url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
#     r = requests.get(url)
#     data = r.json()
#     a = {}
#     for i in data:
#         if i["Ccy"] == "USD":
#             a["USD"] = float(i["Rate"])
#
#         elif i["Ccy"] == "EUR":
#             a["EUR"] = float(i["Rate"])
#
#         elif i["Ccy"] == "RUB":
#             a["RUB"] = float(i["Rate"])
#     return a
#
# def saqlash():
#     a = kurslarni_olish()
#     b = str(date.today())
#     try:
#         with open("kurslar.json", "r") as f:
#             c = json.load(f)
#     except FileNotFoundError:
#         c = []
#     yangi_kurs = {
#         "sana": b,
#         "USD": a["USD"],
#         "EUR": a["EUR"],
#         "RUB": a["RUB"]
#     }
#     c.append(yangi_kurs)
#     with open("kurslar.json", "w") as f:
#         json.dump(c, f)
#
#     print("Bugungi kurslar:")
#     print(f"USD: {a['USD']}")
#     print(f"EUR: {a['EUR']}")
#     print(f"RUB: {a['RUB']}")
# saqlash()
#3
# import requests
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
#     "latitude": 41.2995,
#     "longitude": 69.2401,
#     "daily": "temperature_2m_max,temperature_2m_min",
#     "timezone": "Asia/Tashkent",
#     "forecast_days": 7
# }
# r = requests.get(url)
# data = r.json()
# dates = data["daily"]["time"]
# max_temp = data["daily"]["temperature_2m_max"]
# min_temp = data["daily"]["temperature_2m_min"]
#
# print("Toshkent - 7 kunlik ob-havo")
# print("-" * 45)
# print(f"{'Sana':<15}{'Max °C':<10}{'Min °C':<10}")
# print("-" * 45)
# for i in range(7):
#     print(f"{dates[i]:<15}{max_temp[i]:<10}{min_temp[i]:<10}")
#4
# import requests
#
# url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/XYZ/"
# r = requests.get(url)
# print("Status code:", r.status_code)
# print("Response:", r.text)
# data = r.json()
# print(data)




